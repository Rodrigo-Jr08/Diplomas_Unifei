CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE TABLE schema_versions (
    id                  bigserial PRIMARY KEY,
    version             text NOT NULL,
    package_name        text NOT NULL,
    file_name           text NOT NULL,
    sha256              text NOT NULL CHECK (sha256 ~ '^[0-9a-f]{64}$'),
    source              text,
    retrieved_at        timestamptz NOT NULL DEFAULT now(),
    UNIQUE (version, file_name)
);

CREATE TABLE institutions (
    id                  bigserial PRIMARY KEY,
    name                text NOT NULL,
    codigo_mec          text NOT NULL CHECK (codigo_mec ~ '^[0-9]+$'),
    cnpj                char(14) NOT NULL CHECK (cnpj ~ '^[0-9]{14}$'),
    active              boolean NOT NULL DEFAULT true,
    created_at          timestamptz NOT NULL DEFAULT now(),
    UNIQUE (codigo_mec),
    UNIQUE (cnpj)
);

CREATE TABLE courses (
    id                  bigserial PRIMARY KEY,
    institution_id      bigint NOT NULL REFERENCES institutions(id),
    name                text NOT NULL,
    codigo_curso_emec   text CHECK (codigo_curso_emec IS NULL OR codigo_curso_emec ~ '^[0-9]+$'),
    modality             text,
    degree               text,
    title                text,
    curriculum_code      text,
    active               boolean NOT NULL DEFAULT true,
    created_at           timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE students (
    id                  bigserial PRIMARY KEY,
    academic_id         text NOT NULL,
    name                text NOT NULL,
    social_name         text,
    cpf                 char(11) NOT NULL CHECK (cpf ~ '^[0-9]{11}$'),
    birth_date          date,
    created_at           timestamptz NOT NULL DEFAULT now(),
    UNIQUE (academic_id),
    UNIQUE (cpf)
);

CREATE TYPE diploma_issue_kind AS ENUM (
    'PRIMEIRA_VIA',
    'SEGUNDA_VIA_NATO_FISICO',
    'DECISAO_JUDICIAL',
    'NSF'
);

CREATE TYPE diploma_status AS ENUM (
    'RASCUNHO',
    'VALIDADO_XSD',
    'AGUARDANDO_ASSINATURA',
    'ASSINADO',
    'ATIVO',
    'ANULADO'
);

CREATE TABLE diploma_processes (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    student_id          bigint NOT NULL REFERENCES students(id),
    course_id           bigint NOT NULL REFERENCES courses(id),
    issuer_id           bigint NOT NULL REFERENCES institutions(id),
    registrar_id        bigint REFERENCES institutions(id),
    issue_kind          diploma_issue_kind NOT NULL,
    xsd_version         text NOT NULL,
    nonce               char(44) NOT NULL CHECK (nonce ~ '^[0-9]{44}$'),
    virtual_id          char(48) NOT NULL UNIQUE,
    diploma_id          char(47) NOT NULL UNIQUE,
    registration_id     char(48) UNIQUE,
    request_id          char(50) NOT NULL UNIQUE,
    validation_code     text UNIQUE,
    status              diploma_status NOT NULL DEFAULT 'RASCUNHO',
    public_url          text UNIQUE,
    source_diploma_date date,
    created_at          timestamptz NOT NULL DEFAULT now(),
    validated_at        timestamptz,
    signed_at           timestamptz,
    registered_at       timestamptz,
    revoked_at          timestamptz,
    UNIQUE (xsd_version, nonce)
);

CREATE TABLE xml_artifacts (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    diploma_process_id  uuid NOT NULL REFERENCES diploma_processes(id),
    artifact_kind       text NOT NULL,
    mime_type           text NOT NULL DEFAULT 'application/xml',
    sha256              text NOT NULL CHECK (sha256 ~ '^[0-9a-f]{64}$'),
    byte_size           bigint NOT NULL CHECK (byte_size >= 0),
    object_key          text NOT NULL,
    created_at          timestamptz NOT NULL DEFAULT now(),
    UNIQUE (diploma_process_id, artifact_kind, sha256)
);

CREATE TABLE signatures (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    xml_artifact_id     uuid NOT NULL REFERENCES xml_artifacts(id),
    signer_role         text NOT NULL,
    signer_cpf          char(11),
    signer_cnpj         char(14),
    policy_oid          text,
    policy_name         text,
    certificate_subject text,
    certificate_serial  text,
    signed_at           timestamptz,
    validation_state    text NOT NULL,
    validation_detail   text,
    created_at          timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE supporting_documents (
    id                  uuid PRIMARY KEY DEFAULT gen_random_uuid(),
    diploma_process_id  uuid NOT NULL REFERENCES diploma_processes(id),
    document_type       text NOT NULL,
    sha256              text NOT NULL CHECK (sha256 ~ '^[0-9a-f]{64}$'),
    byte_size           bigint NOT NULL CHECK (byte_size >= 0),
    object_key          text NOT NULL,
    created_at          timestamptz NOT NULL DEFAULT now(),
    UNIQUE (diploma_process_id, document_type, sha256)
);

CREATE TABLE audit_events (
    id                  bigserial PRIMARY KEY,
    diploma_process_id  uuid NOT NULL REFERENCES diploma_processes(id),
    event_type          text NOT NULL,
    actor_id            text,
    event_payload       jsonb NOT NULL DEFAULT '{}'::jsonb,
    occurred_at         timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX idx_diploma_status ON diploma_processes(status);
CREATE INDEX idx_diploma_student ON diploma_processes(student_id);
CREATE INDEX idx_audit_diploma_time ON audit_events(diploma_process_id, occurred_at);

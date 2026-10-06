from diploma_mec.ids import DiplomaIds, generate_nonce, validation_code


def test_nonce_has_44_digits():
    nonce = generate_nonce()
    assert len(nonce) == 44
    assert nonce.isdigit()


def test_id_family_shares_nonce():
    ids = DiplomaIds.from_nonce("1" * 44)
    assert ids.virtual_id.endswith(ids.nonce)
    assert ids.diploma_id.endswith(ids.nonce)
    assert ids.registration_id.endswith(ids.nonce)
    assert ids.request_id.endswith(ids.nonce)


def test_validation_code_shape():
    code = validation_code("584", "584")
    a, b, c = code.split(".")
    assert a == "584"
    assert b == "584"
    assert len(c) == 12
    int(c, 16)

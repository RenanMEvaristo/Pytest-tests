import pytest
from src.validator import Validator


def test_validate_email_sucess():
    validator = Validator()
    result = validator.validate_email("test@example.com")
    assert result is True


def test_validate_email_fails_withouth_at_symbol():
    validator = Validator()
    result = validator.validate_email("invalid-email.com")
    assert result is False


def test_validate_email_fails_without_dot():
    validator = Validator()
    result = validator.validate_email("invalid-email@emailcom")
    assert result is False


def test_validate_email_fails_without_dot_after_at():
    validator = Validator()
    result = validator.validate_email("invalid.email@emailcom")
    assert result is False


def test_validate_password_length_sucess():
    validator = Validator()
    result = validator.validate_password("12345678")
    assert result is True


def test_validate_password_length_fail():
    validator = Validator()
    result = validator.validate_password("12345")
    assert result is False


def test_validate_password_with_number():
    validator = Validator()
    result = validator.validate_password("juvenal1")
    assert result is True


def test_validate_password_without_number():
    validator = Validator()
    result = validator.validate_password("juvenall")
    assert result is False


def test_validate_email_fails_with_multiple_at_symbols():
    validator = Validator()
    result = validator.validate_email("user@@email.com")
    assert result is False

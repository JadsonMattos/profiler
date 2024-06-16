from typing import Callable
from unittest.mock import MagicMock, patch

import pytest
from pytest_dependency import (
    assert_fails_with_broken_asset,
    assert_fails_with_missing_feature_usage,
    get_skip_markers,
    get_test_assessment_configs,
    run_pytest_quietly,
)

from pro_filer.actions.main_actions import find_duplicate_files  # specific
from tests.actions import test_find_duplicate_files  # specific
from tests.trybe import find_duplicate_mocks  # specific

TA_CFG = get_test_assessment_configs(
    find_duplicate_files,
    find_duplicate_mocks,
    test_find_duplicate_files,
)


pytestmark = get_skip_markers(TA_CFG)


@pytest.mark.dependency()
def test_students_sanity_check():
    return_code = run_pytest_quietly([TA_CFG.STUDENT_TEST_FILE_PATH])

    if return_code != pytest.ExitCode.OK:
        pytest.skip(
            f"Seus testes em {TA_CFG.STUDENT_TEST_FILE_PATH} "
            "ainda não estão passando! "
            "Verifique-os e tente novamente."
        )


@pytest.mark.dependency(depends=["test_students_sanity_check"])
@pytest.mark.parametrize(
    "broken_asset",
    TA_CFG.BROKEN_ASSETS_LIST,
)
def test_assess_students_find_duplicate(broken_asset: Callable):
    with patch(TA_CFG.PATCH_TARGET, broken_asset):
        return_code = run_pytest_quietly([TA_CFG.STUDENT_TEST_FILE_PATH])

    assert_fails_with_broken_asset(broken_asset, return_code, TA_CFG)


def test_assess_students_find_duplicate_tmp_path():
    @pytest.fixture
    def mock_tmp_path():
        return MagicMock()

    with patch("_pytest.tmpdir.tmp_path", mock_tmp_path):
        return_code = run_pytest_quietly([TA_CFG.STUDENT_TEST_FILE_PATH])

    assert_fails_with_missing_feature_usage(
        "fixture 'tmp_path'", return_code, TA_CFG
    )


@pytest.mark.dependency(
    depends=[
        "test_assess_students_find_duplicate",
        "test_assess_students_find_duplicate_tmp_path",
    ],
    include_all_instances=True,
)
def test_assess_students_find_duplicate_final():
    pass

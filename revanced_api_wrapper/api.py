from typing import Any
from .constants import ENDPOINTS

class ReVancedAPI(object):

    @staticmethod
    def rate_limit() -> Any:
        return ENDPOINTS['rate_limit'].get().json()

    @staticmethod
    def is_rate_limited() -> bool:
        return ReVancedAPI.rate_limit()['remaining'] == 0

    @staticmethod
    def _check_rate_limited() -> None:
        if ReVancedAPI.is_rate_limited():
            raise RuntimeError('User is rate limited, try again later.')

    @staticmethod
    def get_announcements(from_oldest: bool = False) -> list[Any]:
        ReVancedAPI._check_rate_limited()
        announcements: list[Any] = ENDPOINTS['announcements'].get().json()
        if not from_oldest:
            announcements = sorted(announcements, key = lambda ann: ann['id'], reverse = True)
        return announcements

    @staticmethod
    def get_announcements_length() -> int:
        ReVancedAPI._check_rate_limited()
        return len(ReVancedAPI.get_announcements())

    @staticmethod
    def get_nth_announcement(n: int) -> Any:
        ReVancedAPI._check_rate_limited()
        return ReVancedAPI.get_announcements()[n]

    @staticmethod
    def get_latest_patches_release() -> Any:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['patches_latest'].get().json()

    @staticmethod
    def get_latest_patches_version() -> str:
        ReVancedAPI._check_rate_limited()
        return str(ENDPOINTS['patches_latest_version'].get().json()['version']).lstrip('v')

    @staticmethod
    def get_latest_patches_list() -> list[Any]:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['patches_latest_list'].get().json()

    @staticmethod
    def get_patches_for_package(package_name: str) -> Any:
        ReVancedAPI._check_rate_limited()
        return [patch for patch in ReVancedAPI.get_latest_patches_list() if not patch['compatiblePackages'] or package_name in patch['compatiblePackages']]

    @staticmethod
    def get_patches_pgp_key() -> str:
        ReVancedAPI._check_rate_limited()
        return str(ENDPOINTS['patches_keys'].get().json()['patches_public_key']).strip()

    @staticmethod
    def get_latest_manager_release() -> Any:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['manager_latest'].get().json()

    @staticmethod
    def get_latest_manager_version() -> str:
        ReVancedAPI._check_rate_limited()
        return str(ENDPOINTS['manager_latest_version'].get().json()['version']).lstrip('v')

    @staticmethod
    def get_contributors() -> list[Any]:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['contributors'].get().json()

    @staticmethod
    def get_team_members() -> list[Any]:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['team'].get().json()

    @staticmethod
    def get_about() -> Any:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['about'].get().json()

    @staticmethod
    def is_up() -> bool:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['ping'].head().ok
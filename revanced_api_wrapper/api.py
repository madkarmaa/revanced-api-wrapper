from os import path
from typing import Any
from urllib.request import urlretrieve
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
    def announcements(from_oldest: bool = False) -> list[Any]:
        ReVancedAPI._check_rate_limited()
        announcements: list[Any] = ENDPOINTS['announcements'].get().json()
        if not from_oldest:
            announcements = sorted(announcements, key = lambda ann: ann['id'], reverse = True)
        return announcements

    @staticmethod
    def announcements_length() -> int:
        ReVancedAPI._check_rate_limited()
        return len(ReVancedAPI.announcements())

    @staticmethod
    def get_nth_announcement(n: int) -> Any:
        ReVancedAPI._check_rate_limited()
        return ReVancedAPI.announcements()[n]

    @staticmethod
    def latest_patches_release() -> Any:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['patches_latest'].get().json()

    @staticmethod
    def latest_patches_version() -> str:
        ReVancedAPI._check_rate_limited()
        return str(ENDPOINTS['patches_latest_version'].get().json()['version']).lstrip('v')

    @staticmethod
    def latest_patches_list() -> list[Any]:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['patches_latest_list'].get().json()

    @staticmethod
    def get_patches_for_package(package_name: str) -> list[Any]:
        ReVancedAPI._check_rate_limited()
        return [
            patch
            for patch
            in ReVancedAPI.latest_patches_list()
            if not patch['compatiblePackages']
            or package_name in patch['compatiblePackages']
        ]

    @staticmethod
    def patches_pgp_key() -> str:
        ReVancedAPI._check_rate_limited()
        return str(ENDPOINTS['patches_keys'].get().json()['patches_public_key']).strip()

    @staticmethod
    def _download_file(download_url: str, out_dir: str = './') -> bool:
        ReVancedAPI._check_rate_limited()

        file_path: str = path.normpath(path.abspath(path.join(out_dir, download_url.split('/').pop())))

        try:
            urlretrieve(download_url, file_path)
        except:
            return False
        else:
            return True

    @staticmethod
    def download_patches_jar(out_dir: str = './') -> bool:
        download_url: str = [
            asset
            for asset
            in ReVancedAPI.latest_patches_release()['assets']
            if asset['name'] == 'PATCHES'
        ][0]['download_url']
        return ReVancedAPI._download_file(download_url, out_dir)

    @staticmethod
    def download_integrations_apk(out_dir: str = './') -> bool:
        download_url: str = [
            asset
            for asset
            in ReVancedAPI.latest_patches_release()['assets']
            if asset['name'] == 'INTEGRATION'
        ][0]['download_url']
        return ReVancedAPI._download_file(download_url, out_dir)

    @staticmethod
    def latest_manager_release() -> Any:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['manager_latest'].get().json()

    @staticmethod
    def latest_manager_version() -> str:
        ReVancedAPI._check_rate_limited()
        return str(ENDPOINTS['manager_latest_version'].get().json()['version']).lstrip('v')

    @staticmethod
    def download_manager_apk(out_dir: str = './') -> bool:
        download_url: str = ReVancedAPI.latest_manager_release()['assets'][0]['download_url']
        return ReVancedAPI._download_file(download_url, out_dir)

    @staticmethod
    def contributors() -> list[Any]:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['contributors'].get().json()

    @staticmethod
    def is_contributor(github_username: str) -> bool:
        return github_username in set(
            # https://www.leocon.dev/blog/2021/09/how-to-flatten-a-python-list-array-and-which-one-should-you-use/#11-list-comprehension
            [
                contributor['name']
                for contributors
                in [
                    project['contributors']
                    for project
                    in ReVancedAPI.contributors()
                ]
                for contributor
                in contributors
            ]
        )

    @staticmethod
    def team_members() -> list[Any]:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['team'].get().json()

    @staticmethod
    def is_team_member(github_username: str) -> bool:
        ReVancedAPI._check_rate_limited()
        return github_username in [
            member['name']
            for member
            in ReVancedAPI.team_members()
        ]

    @staticmethod
    def about() -> Any:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['about'].get().json()

    @staticmethod
    def is_up() -> bool:
        ReVancedAPI._check_rate_limited()
        return ENDPOINTS['ping'].head().ok
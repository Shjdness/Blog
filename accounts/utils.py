import typing
from datetime import timedelta

from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext

from djangoblog.utils import send_email

_code_ttl = timedelta(minutes=5)


def send_verify_email(to_mail: str, code: str, subject: str = _("Verify Email")):
    """发送重设密码验证码
    Args:
        to_mail: 接受邮箱
        subject: 邮件主题
        code: 验证码
    """
    html_content = _(
        f"You are resetting the password, the verification code is：{code}, valid within 5 minutes, please keep it properly")
    send_email([to_mail], subject, html_content)


def verify(email: str, code: str) -> typing.Optional[str]:
    """验证code是否有效
    Args:
        email: 请求邮箱
        code: 验证码
    Return:
        如果有错误就返回错误str
    Node:
        这里的错误处理不太合理，应该采用raise抛出
        否测调用方也需要对error进行处理
    """
    cache_code = get_code(email)
    if cache_code != code:
        return gettext("Verification code error")


def set_code(email: str, code: str):
    """设置code"""
    cache.set(email, code, _code_ttl.seconds)


def get_code(email: str) -> typing.Optional[str]:
    """获取code"""
    return cache.get(email)

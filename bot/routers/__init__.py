__all__ = ("router",)

from aiogram import Router
from .calback_handlers import router as callback_router
from .commands import router as commands_router
from .handlers import router as handlers_router

router = Router(name=__name__)

router.include_routers(callback_router,
                       commands_router,
                       handlers_router,
                       )

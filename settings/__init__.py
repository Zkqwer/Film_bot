from settings.config_reader import config
from aiogram import F

KINOPOISK_API = config.kinopoisk_token.get_secret_value()
TELEGRAM_BOT_TOKEN = config.bot_token.get_secret_value()

HEADERS = {'X-API-KEY': KINOPOISK_API,
           'Content-Type': 'application/json'}

RELATION_TYPES = {
    'REMAKE': 'ремейк',
    'SEQUEL': 'сиквел',
    'PREQUEL': 'приквел'
}

any_media_filter = (F.photo | F.video | F.document | F.sticker | F.audio | F.voice | F.video_note | F.location |
                    F.contact | F.animation | F.dice | F.poll)

stickers = ['CAACAgIAAxkBAAIT5GYqiXN49mZafCWffURS3RgDHH5AAAJ6IgAC6GV5SrLcytH3agAB9DQE',
            'CAACAgIAAxkBAAIT5WYqiXgr8tBaaxMGHgJQdMOnLXrjAALGKgAC3DGYS0DW5-PX_pWVNAQ',
            'CAACAgIAAxkBAAIT5mYqiXoPSEbgarXvLJ6byB-siB8UAALVIgACOvD4S6pWF7g7i40TNAQ',
            'CAACAgIAAxkBAAIT52YqiX6YpWG2k-SirfuHu6qPBRVQAAIMIQAC8qTJSHC5SxHhstNJNAQ',
            'CAACAgIAAxkBAAIT6GYqiYC0hA_t_5IVGNNis-dLhAEsAAJhJAACMxhISWUzbsrXdHccNAQ',
            'CAACAgIAAxkBAAIT6WYqiYHn3ufQLitRTyD9ucr_wvEvAAK_SAACTP05SEBTs8P-xxbINAQ',
            'CAACAgIAAxkBAAIT6mYqiYNx83eMsSRwM1kvbefLrNYmAAIePwACQhw4SBKvfPu_AAElTzQE',
            'CAACAgIAAxkBAAIT62YqiYXN2Zp0JF-y9nEGG7syXHY-AAKHQgACok84SPmWETm9zpl3NAQ',
            'CAACAgIAAxkBAAIT7GYqiYfHBXFcjQ_-ZDuyfjgZc318AAIpRgACkyo4SLWzI0KRmy49NAQ',
            'CAACAgIAAxkBAAIT7WYqiYhd2XAxh049yJ9vS9_JbkbpAAIXQgACm6g5SJfkAp-BXnUMNAQ',
            'CAACAgIAAxkBAAIT7mYqiYrb6T1Hn6G1KcbtF-4BzqGTAALDQwACg-U4SAAB68OPqTfb1DQE',
            'CAACAgIAAxkBAAIT72YqiYuP3oHPeNIKVA0Q2QvHg_mlAAJfSgAC-0owSJ2MAdXqkoy_NAQ',
            'CAACAgIAAxkBAAIT8GYqiY0yeXxwqOY76lpQ00oVVDMVAAJqTAACDz05SNDU0ezCmYNTNAQ',
            'CAACAgIAAxkBAAIT8WYqiY5noMC552nH9KoiODoyXhSeAAIdNwACYROBSM15aCEvDjMqNAQ',
            'CAACAgIAAxkBAAIT8mYqiZDxz8bRsSN1LiEAAQYffmyxMAACpzQAAjisgUi65TKVYgY3VzQE',
            'CAACAgIAAxkBAAIT82YqiZT_WEMFZqZP8VdaukDVOZXpAAL6NQACMFKBSM1oUiZzBlLkNAQ',
            'CAACAgIAAxkBAAIT9GYqiZlYGTDVnB48P6FonhS-E4BmAAKIOQACxIzwS22Qe7rEY9GQNAQ',
            'CAACAgIAAxkBAAIT9WYqiZvOTucpkqETBaMnTIjpcJIWAAJjNAAC5oD4S119AAEHDS-nYDQE',
            'CAACAgIAAxkBAAIT9mYqiZ2D5I4QkDvsyvxPaeFJMdd_AALpNQACZn34Syh5a6sMdNzoNAQ',
            'CAACAgIAAxkBAAIT92YqiaD68SdKhUcvGPIycjWNKMI1AAIsMQACPOppSqkzdrj3VtXKNAQ',
            'CAACAgIAAxkBAAIT-GYqiaRF0GGj_U_8vQABO_EZG8dJuwACrzIAAt20sEuPeIdh_Lp1LTQE',
            'CAACAgIAAxkBAAIT-WYqiaXofCnBRniNDshUwkhLZ5u_AAJNLwACyLKwS9ZeabF2srcMNAQ',
            'CAACAgIAAxkBAAIT-mYqiaayjVjNFQiPol7SIbhiSQAB3QACkzEAAq00sEstuXiJH438NjQE',
            'CAACAgIAAxkBAAIT-2YqiaicmOdmge_WLozk71zafm_XAAJEGAAC3-_pSedVTBc8_PcPNAQ',
            'CAACAgIAAxkBAAIT_GYqiarJr_of8hkKVdUK_TApNxsKAAKEJgACKYVxSq1Qq0467bb7NAQ',
            'CAACAgIAAxkBAAIT_WYqiatDuCQa-VEiJ6BwSF-ny9MjAALaIQACJaVJSbyZbwGMFFOXNAQ',
            'CAACAgIAAxkBAAIT_mYqia3glIyzj0hHXXPRQ4ku9rSpAAJyIwAC7C3BS5Nnl82l71FeNAQ',
            'CAACAgIAAxkBAAIT_2Yqia_AbHFYubuWEEPFNAEhGyrMAAJAIgACerZgS6v56jZzNr_-NAQ',
            'CAACAgIAAxkBAAIUAAFmKomxpP_9GQzGdWHuqQOgqb_SrgACmBoAAovK6UmeguZhOhueXTQE',
            'CAACAgIAAxkBAAIUAWYqibImqTvjNk6EglWCkFi4CLcpAALHGgACDpjISCjp0dk3ziwnNAQ',
            'CAACAgIAAxkBAAIUAmYqibQsc9CNSRxbG4h6M8Xwi6E8AAKcGgACbcrhSaJrx6PshMkVNAQ',
            'CAACAgIAAxkBAAIUA2Yqibhj8Rfc63SqNEmfOiEoiKdlAAI_UAACW545SJH34uT2-xTzNAQ',
            'CAACAgIAAxkBAAIUBGYqiblOlb6nohJ2jaW6rAolURLHAAKWRwADUDhICVxdAtpIzT00BA',
            'CAACAgIAAxkBAAIUBWYqibucnH0mcVlrSPaMwTXXfWt5AAI8SQAC0684SIwvHFQjH299NAQ',
            'CAACAgIAAxkBAAIUBmYqib2SC8fs71KahiYMngJ4gKnRAAIdSAACPQQ4SH5QT4BkkH77NAQ',
            'CAACAgIAAxkBAAIUB2Yqib4HsYH-cowVzeW38rK7wzcPAAIkQwAChFE5SFDcMtC1WYCdNAQ',
            'CAACAgIAAxkBAAIUCGYqicRfuGoBmYMLreg0QDRuf2QxAAIfQQACOsM4SAP23XG0VQgONAQ',
            'CAACAgIAAxkBAAIUCWYqicgb4woEW-bXSB14W0cYWsCSAAIJTwAC_T45SLR0A1l7P_3-NAQ',
            'CAACAgIAAxkBAAIUCmYqicnMfQ72A42KdBtVLFNObzQhAAJvSQACuEg5SB5OWeJfYO69NAQ',
            'CAACAgIAAxkBAAIUC2YqictZgAEEwxdaazUscX2ZEHfxAAJpRwACpCQ5SJWUW_YwTbywNAQ',
            'CAACAgIAAxkBAAIUDGYqic0HFFkS5dMIMJUOKraQFkeOAAJxRgAC2uYxSJs6VvnqXYYQNAQ',
            'CAACAgIAAxkBAAIUDWYqic98dm0014Wu3iH1h2FnnSItAAJ7RQACxRc5SMVALrPqoO1rNAQ',
            'CAACAgIAAxkBAAIUDmYqidDV8gzadczW3w4EWWdWJ2NhAAKGRQAC7po5SIxemVnizzYfNAQ',
            'CAACAgIAAxkBAAIUD2YqidGWtIgTEVvh1kNiQQ_ueAzaAALLQwACoY0xSEXAzEmHmiF3NAQ',
            'CAACAgIAAxkBAAIUEGYqidLD9YiqFdQ3S1SDJcr9elf9AAI-RAACgwgwSK6TgghrubwxNAQ',
            'CAACAgIAAxkBAAIUEWYqidNuAuvIH3i1gIG1HMEgRtDUAAJcRQAC5Es5SC1wWbTczpneNAQ',
            'CAACAgIAAxkBAAIUEmYqidRAT8A7KHW5soICytqvxPE8AAJtRgACR-EwSEiKEWKovJTZNAQ',
            'CAACAgIAAxkBAAIUE2YqidU-mG4I1hElowMP6YHktDqRAAKCSwAC5b0wSG0kHkw1B8HvNAQ',
            'CAACAgIAAxkBAAIUFGYqidlXf4_V7J90SHZ_h0z1eUu5AAK-PQACfFBxSP7v1Wk7jVMqNAQ',
            'CAACAgIAAxkBAAIUFWYqidvB9hXmERinJO5ynDx99IcUAAKUQAAC-fNxSOgFZTEV1vYSNAQ',
            'CAACAgIAAxkBAAIUFmYqid11rWCxxppkPcN9Mz8rKmoJAALnTQACPTdxSLyJ6Mv1EVs5NAQ',
            'CAACAgIAAxkBAAIUF2YqieCJ0y-jaGloSd7e6K_G5Ul5AAKFSQACGmZxSOWM_-9N2tFoNAQ',
            'CAACAgIAAxkBAAIUGGYqieeJmmlLfgaDr_JhimqEyQW3AAK1PAACBUZ4SOiIo_n6RHoXNAQ',
            'CAACAgIAAxkBAAIUGWYqielzciXmhvuc22c7pxAYMu6aAAL3QgACCa9wSG7zPvrbRJztNAQ',
            'CAACAgIAAxkBAAIUGmYqieuRu9JJtSBGXTn5ObZT5vIgAALLQQACDQVxSAEMN5gfvI0CNAQ',
            'CAACAgIAAxkBAAIUG2Yqie0QaArlhpGpI_epYj7wweZDAAIWQwACjpRxSMSJxgyZUO4nNAQ',
            'CAACAgIAAxkBAAIUHGYqie7mR9a9mgjoc0HlmfotExrGAAJPPwACIzlxSCXSDDX3FBTuNAQ',
            'CAACAgIAAxkBAAIUHWYqifAjgFQy5x5LLbRNHUzylTMlAAIQPAACnOhwSPGcRIvNdnhfNAQ',
            'CAACAgIAAxkBAAIUHmYqifG8_VlOPt2i8W-w7T55le4ZAAKwNgACQdZ4SF-_aS2j0unqNAQ',
            'CAACAgIAAxkBAAIUH2YqifLksGfmKBTZ_bBbGgGoBgf8AALZNwACi7d4SDMbvFtOfnCUNAQ',
            'CAACAgIAAxkBAAIUIGYqifMvRwt_B7bP85JjejMp7RmhAAKuNwAC7eB5SD3JlO7Xs6E1NAQ',
            'CAACAgIAAxkBAAIUIWYqifSS7T6XCDv_2qzs7R0MchgsAAKhNgACeF1xSLnQI02W5a4yNAQ',
            'CAACAgIAAxkBAAIUImYqifZ2j7uWP4KdZVuQq4tWmPXvAAIgOwACEoBxSLlgQQ6JD-LDNAQ',
            'CAACAgIAAxkBAAIUI2YqifsO024w-3Q6LA6_iGPzUDbRAAJWTgACk41wSM_IH1Ci6lILNAQ',
            'CAACAgIAAxkBAAIUJGYqif1U8_-DNPVYK7t_kGBLoaRHAAJSWgACGSJwSGarFsQr_OMVNAQ',
            'CAACAgIAAxkBAAIUJWYqif6PykeQf5IRHswWBIo61-80AALhOAACNdFxSEe-E3QKPDxxNAQ',
            'CAACAgIAAxkBAAIUJmYqigABVQGzizcPL1xvDTFjgYyuiQAChTwAAnrUcEg6foc5zjhinjQE',
            'CAACAgIAAxkBAAIUJ2YqigPbIy5vo8mFIxSj65sTh1VGAAKnOgACZD9xSEMMgPC7wx2NNAQ',
            'CAACAgIAAxkBAAIUKGYqigT9LwrmwgHvxCZ8-D08eMYpAAI4QAAC3bBwSFoJSjGC-kcMNAQ',
            'CAACAgIAAxkBAAIUKWYqigpHlJ3c1AjqCgUVs2E-mwpDAAIyMwACHLzRSXkN0BRGUKbENAQ',
            'CAACAgIAAxkBAAIUKmYqig-c1rXrGZYpWSB_TObs80fSAAJOJgAC-zdQSRHqwqcXa7b3NAQ',
            'CAACAgIAAxkBAAIUK2YqihA2Y9As7CgGkmZ1NJiXwuuxAAIuIwACQQGASTyVbQ9-iINVNAQ',
            'CAACAgIAAxkBAAIULGYqihsUxKvvc7FTTMwK2uc-ng7aAALXJAACweXhSfNIErZOP5AtNAQ',
            'CAACAgIAAxkBAAIULWYqih-7s0GHS77kzyJvqhXRyx1AAAKDJQACElkpSqakdS9Dd7VFNAQ',
            'CAACAgIAAxkBAAIULmYqiiH0j-V4H2q-mDcDyw2Jl0peAAJOLwAC-PohSnSAN4lUwARcNAQ',
            'CAACAgIAAxkBAAIUL2YqiiKRmKboC2o3ivcTCIZXvjsoAAL5KwACjF4gSpJGs3qY4XUDNAQ',
            'CAACAgIAAxkBAAIUMGYqiiXfqkC_tOkal498JlJ0AoroAALtIQAC6gEoSizf-Hl8eoqtNAQ',
            'CAACAgIAAxkBAAIUMWYqiipT16jAoNzJLyTUQxuFeVsgAAIWIwACARKhSvBtgGbDrbRiNAQ',
            'CAACAgIAAxkBAAIUMmYqii6W7YzNMYOvvSq1vf8F1-pBAALXGwACsBioShenfmLGQyxjNAQ',
            'CAACAgIAAxkBAAIUM2YqijBvjPaeWJP3uCpB0zskvMdQAAJtGwAChbWpSlycFZ97AeJGNAQ',
            'CAACAgIAAxkBAAIUNGYqijKTDLibAxq8nqkwR0NX5lZpAAJhJAACv5KgSm1tXIr6wAuONAQ',
            'CAACAgIAAxkBAAIUNWYqijRr8x5t8k7A6fSR9aoMxIOaAALWIgACmuOhSgz0lavJAoy2NAQ',
            'CAACAgIAAxkBAAIUNmYqijYEWcS-sUkfoR1J9BQ4HAptAAJZHwACQx-oStqMzEcY6tP9NAQ',
            'CAACAgIAAxkBAAIUN2YqijhVeOoYfMFJwUSt7IhIsW_iAALMIwACbsyxSk5TeQHYtuQFNAQ',
            'CAACAgIAAxkBAAIUOGYqikHO377Heeow9Dt52npzCp_OAAJ3HQACBUGxSm0TcCV-yMYoNAQ',
            'CAACAgIAAxkBAAIUOWYqikPSz-eBk4dmJhNESBJa35n0AALNIQAC403BSvIuzZ_CK75yNAQ',
            'CAACAgIAAxkBAAIUOmYqikTX0McIWMRN1_w3SxbRKTfKAAKNIgACAr_ASpbAaLKjn-EUNAQ',
            'CAACAgIAAxkBAAIUO2YqikfeYGJ-MGKQOWDki1zSb5gLAAI4IAAC-nnBSqsS4UHVPflPNAQ',
            'CAACAgIAAxkBAAIUPGYqikjKTqF6zGn9VH72nXghn8pxAAK1JgACylCoS630yh0o6TcMNAQ',
            'CAACAgIAAxkBAAIUPWYqikq4208urICOsM3dE-p6uDuDAAMhAAKhmfhKNJgWuNCa4Rw0BA',
            'CAACAgIAAxkBAAIUPmYqiktuk3gZ9gNa7MYlNPzsH26RAALPIQAC_8yAS9r4ioS1NGuNNAQ',
            'CAACAgIAAxkBAAIUP2Yqik1RETaVHihvQJRxZfreR7jbAAKvLAACcqVwSKpncctrOqImNAQ',
            'CAACAgIAAxkBAAIUQGYqik6tDqfbRAY-MtHAkHaVN3lhAALAHQACsmQQSP5mGFl3P3P6NAQ',
            'CAACAgIAAxkBAAIUQWYqik_T-8dpvIp9RF_TdyXAI9C_AAJ2KwACIOsISG950rZBDzBeNAQ',
            'CAACAgIAAxkBAAIUQmYqilHRLvEtxNeSeS6lhElSvXhSAAKMHgACwk-xS-Ohlnpar0PVNAQ',
            'CAACAgIAAxkBAAIUQ2YqimcNWyTkRWPHq6PRIVFc17AxAAItLgAC5gi4S0NOukfYo41uNAQ',
            'CAACAgIAAxkBAAIURGYqin-hIyYoXeQWevwgNSZEYNigAAKnPwACt9FRSu4n4qR9sbv4NAQ',
            'CAACAgIAAxkBAAIURWYqioKrqy7oFRU2dO_mXnVUj6f7AAIJIwACUqAJS8cR6FmiawLTNAQ',
            'CAACAgIAAxkBAAIURmYqio9bnsw2O0Xs8Ap7-iLfND8FAAJ8FgAC1E5xSn32Fm8mRzqnNAQ',
            'CAACAgIAAxkBAAIUR2YqipGtDx2o8TfVRxxp3VDB0cQEAAKQGgACqHphSjuIm4OjdPMxNAQ',
            'CAACAgIAAxkBAAIUSGYqipJ-_Qf-UK0sRPmgYbUHmBBfAAJYHQACw6ZhSg-0Ub7w9gABlzQE',
            'CAACAgIAAxkBAAIUSWYqipTwkG3iCl8h6K7655aZ_GwWAALXGQACq8ZoSqoXMFYX5AnNNAQ',
            'CAACAgIAAxkBAAIUS2YqitCR2PEGrF_LjZ7LfzUtOR4sAALyEwACd_3oS9_K3QZDK53GNAQ',
            'CAACAgIAAxkBAAIUTGYqitkMv3dmfGqKB-U0b1zL_ZfjAAJJFgACYj_4S-q01q6YGgOGNAQ']

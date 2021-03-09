from hexonet.apiconnector.responsetemplatemanager import ResponseTemplateManager as RTM
from hexonet.apiconnector.responsetemplate import ResponseTemplate as RT


def test_rtmmethods():
    # #.getTemplate()
    rtm = RTM()
    tpl = rtm.getTemplate("IwontExist")
    assert tpl.getCode() == 500
    assert tpl.getDescription() == "Response Template not found"

    # #.getTemplates()
    defaultones = sorted(
        [
            "404",
            "500",
            "error",
            "httperror",
            "invalid",
            "empty",
            "unauthorized",
            "expired",
        ]
    )
    availableones = sorted(rtm.getTemplates().keys())
    assert defaultones == availableones

    # #.isTemplateMatchHash()
    tpl = RT("")
    assert rtm.isTemplateMatchHash(tpl.getHash(), "empty") is True

    # #.isTemplateMatchPlain()
    assert rtm.isTemplateMatchPlain(tpl.getPlain(), "empty") is True

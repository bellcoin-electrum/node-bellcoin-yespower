{
    "targets": [
        {
            "target_name": "bellcoin_yespower",
            "sources": [
                "bellcoin_yespower.cc",
                "yespower-1.0.0/yespower.h",
                "yespower-1.0.0/yespower-opt.c",
                "yespower-1.0.0/sha256.c",
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        }
    ]
}

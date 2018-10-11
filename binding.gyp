{
    "targets": [
        {
            "target_name": "bitzeny_yescrypt",
            "sources": [               
                "bitzeny_yescrypt.cc",
                "yescrypt-0.5/yescrypt.c",
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ],
            "cflags_cc": [
                "-std=c++0x"
            ],
        },
        {
            "target_name": "bitzeny_yespower",
            "sources": [
                "bitzeny_yespower.cc",
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

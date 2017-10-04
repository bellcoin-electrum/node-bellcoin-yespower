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
        }
    ]
}

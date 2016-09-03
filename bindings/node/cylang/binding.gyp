{
  "targets": [
    {
      "variables": {
        "conditions": [
          ["OS=='win' and target_arch=='ia32'", {
            "frida_host_msvs": "Win32-<(CONFIGURATION_NAME)",
          }],
          ["OS=='win' and target_arch=='x64'", {
            "frida_host_msvs": "x64-<(CONFIGURATION_NAME)",
          }],
        ],
      },
      "target_name": "cylang_binding",
      "sources": [
        "addon.cpp",
      ],
      "include_dirs": [
        "../../..",
        "<!(node -e \"require(\'nan\')\")",
      ],
      "target_conditions": [
        ["OS=='win'", {
          "library_dirs": [
            "../../../build/<(frida_host_msvs)/lib",
          ],
          "libraries": [
            "-lcycript.lib",
          ],
        }, {
          "cflags!": [
            "-fno-exceptions",
          ],
          "cflags_cc!": [
            "-fno-exceptions",
          ],
          "libraries": [
            "../../../../.libs/libcycript.a",
          ],
        }],
        ["OS=='mac'", {
          "xcode_settings": {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            "OTHER_CFLAGS": [
              "-std=c++11",
              "-stdlib=libc++",
              "-mmacosx-version-min=10.7",
            ],
            "OTHER_LDFLAGS": [
              "-Wl,-macosx_version_min,10.7",
              "-Wl,-dead_strip",
              "-Wl,-exported_symbols_list,binding.symbols",
            ],
          },
        }],
        ["OS=='linux'", {
          "cflags": [
            "-std=c++11",
            "-ffunction-sections",
            "-fdata-sections",
          ],
          "ldflags": [
            "-Wl,--gc-sections",
            "-Wl,--version-script",
            "-Wl,../binding.version",
          ],
        }],
      ],
    },
  ],
}

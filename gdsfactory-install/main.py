import subprocess
import sys
import uv


def install_gdsfactory():
    try:
        uv_bin = uv.find_uv_bin()
        subprocess.check_call(
            [
                uv_bin,
                "tool",
                "install",
                "--force",
                "--python",
                "python3.12",
                "gdsfactory@latest",
            ]
        )
        subprocess.check_call([uv_bin, "tool", "update-shell"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install gdsfactory: {e}")
        sys.exit(1)


def main():
    install_gdsfactory()


if __name__ == "__main__":
    main()

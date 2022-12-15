import sys
import atexit
import os


def restart():
    if "HIKKA_DO_NOT_RESTART" in os.environ:
        print("Got in a loop, exiting")
        sys.exit(0)

    print("🔄 Перезавантаження...")

    atexit.register(
        lambda: os.execl(
            sys.executable,
            sys.executable,
            "-m",
            os.path.relpath(
                os.path.abspath(
                    os.path.dirname(
                        os.path.abspath(__file__),
                    ),
                ),
            ),
            *(sys.argv[1:]),
        )
    )

    os.environ["HIKKA_DO_NOT_RESTART"] = "1"

    sys.exit(0)

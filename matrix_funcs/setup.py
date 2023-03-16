from distutils.core import setup, Extension


def main():
    setup(name="matrix_funcs",
          version="1.0.0",
          description="Python interface for the determinant calculation C function",
          author="ppsn",
          author_email="popasena2@ya.ru",
          ext_modules=[Extension("matrix_funcs", ["matrix_funcs.c"])])


if __name__ == "__main__":
    main()

# ghostscript-bin

Ghostscript (`gs`) binary distribution for Python. Install via pip, get a working `gs` command.

```
pip install ghostscript-bin
```

## Usage

### Command line

```bash
gs --version
gs -sDEVICE=pdfwrite -o output.pdf input.ps
```

### Python API

```python
import ghostscript_bin

# Path to the bundled gs binary
ghostscript_bin.gs_path()

# Version string
ghostscript_bin.version()

# Run gs with arguments (wraps subprocess.run)
ghostscript_bin.run(["-sDEVICE=pdfwrite", "-o", "output.pdf", "input.ps"])
```

## Included devices

pdfwrite, ps2write, eps2write, bbox, txtwrite, inkcov,
png (all variants), jpeg, tiff (all variants),
pbm/pgm/pnm/ppm (all variants), and nullpage.

## How it works

The package builds Ghostscript from source using scikit-build-core and CMake's `ExternalProject`. The binary is compiled with `COMPILE_INITS=1` (the default), which embeds all Resource, Init, Font, CMap, and ICC files directly into the binary. This means the installed package is a single self-contained `gs` executable with no external dependencies beyond system libc.

## Platforms

Pre-built wheels are available for:

- Linux x86_64 (manylinux)
- Linux aarch64 (manylinux)
- macOS arm64

## License

AGPL-3.0-or-later (same as Ghostscript itself). See [LICENSE](LICENSE).

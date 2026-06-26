# Contributing

Thanks for improving ascii-cpumap.

## Local setup

```bash
git clone https://github.com/wetair1/ascii-cpumap.git
cd ascii-cpumap
python3 main.py
```

No external dependencies are required.

## Code style

- Keep the project pure Python stdlib.
- Keep `/proc/stat` parsing small and readable.
- Keep the heatmap useful on small terminals.
- Avoid blocking work inside the render loop.
- Document Linux-specific behavior.

## Checks

```bash
python3 -m py_compile main.py
python3 main.py
```

## Commit style

Use short imperative messages, for example:

- `Add core labels`
- `Improve heatmap scale`
- `Document controls`

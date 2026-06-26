# Architecture

ascii-cpumap is a compact curses CPU heatmap built with only the Python standard library.

## Runtime flow

1. The app reads per-core CPU counters from `/proc/stat`.
2. Two snapshots are compared to calculate usage per core.
3. Each usage value is mapped to an ASCII shade or bar.
4. The curses UI redraws the heatmap on every refresh tick.
5. Pressing `q` exits the app.

## Main parts

- `read_cpu_lines()` reads raw counters for every CPU core.
- `usage()` converts two counter snapshots into percentages.
- `shade()` maps usage values to ASCII intensity characters.
- `draw()` owns refresh timing, rendering and keyboard handling.

## Design rules

- Keep dependencies at zero.
- Keep `/proc/stat` parsing isolated.
- Keep the display readable on small terminals.
- Prefer polling over background threads.
- Make Linux-specific assumptions clear in docs.

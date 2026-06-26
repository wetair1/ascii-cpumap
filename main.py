#!/usr/bin/env python3
import curses, time, os


def read_cpu_lines():
    rows = []
    with open('/proc/stat') as f:
        for line in f:
            if line.startswith('cpu') and line[3:4].isdigit():
                parts = list(map(int, line.split()[1:8]))
                idle = parts[3] + parts[4]
                total = sum(parts)
                rows.append((idle, total))
    return rows


def usage(prev, cur):
    out = []
    for a, b in zip(prev, cur):
        idle = b[0] - a[0]
        total = b[1] - a[1]
        out.append(0 if total <= 0 else 100 * (1 - idle / total))
    return out


def block(v):
    chars = ' .:-=+*#%@'
    return chars[min(len(chars)-1, int(v / 100 * (len(chars)-1)))]


def draw(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    prev = read_cpu_lines()
    while True:
        time.sleep(0.5)
        cur = read_cpu_lines(); vals = usage(prev, cur); prev = cur
        h, w = stdscr.getmaxyx()
        cols = max(1, min(len(vals) or 1, w // 12))
        stdscr.erase()
        stdscr.addstr(0, 2, f'ASCII CPUMAP - {len(vals)} cores - q to quit')
        for i, v in enumerate(vals):
            x = 2 + (i % cols) * 12
            y = 2 + (i // cols) * 4
            if y + 2 >= h: break
            cell = block(v) * 8
            stdscr.addstr(y, x, f'CPU{i:<3}')
            stdscr.addstr(y+1, x, cell)
            stdscr.addstr(y+2, x, f'{v:5.1f}%')
        if stdscr.getch() in (ord('q'), ord('Q')): break


if __name__ == '__main__':
    curses.wrapper(draw)

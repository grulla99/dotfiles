# dotfiles

Personal configuration files for macOS development environment.

## What's Included

### Kitty Terminal

Custom [Kitty](https://sw.kovidgoyal.net/kitty/) terminal configuration with:

- **Theme**: Catppuccin Mocha with 70% background opacity and blur
- **Font**: D2Coding, 12pt
- **Tab Bar**: Custom cyberpunk neon style with rotating color palette
- **Layout**: Splits + Stack with macOS-style keybindings
- **Cursor**: Beam cursor with trail effect

#### Key Bindings

| Shortcut | Action |
|----------|--------|
| `Cmd+T` | New tab |
| `Cmd+D` | Vertical split |
| `Cmd+Shift+D` | Horizontal split |
| `Cmd+W` | Close window |
| `Cmd+C/V` | Copy / Paste |
| `Cmd+Z` | Undo (sends Ctrl+_) |
| `Cmd+Left/Right` | Line start / end |
| `Cmd+A` | Delete current line |
| `Cmd+Up/Down` | Scroll to top / bottom |
| `Cmd+Shift+Arrow` | Navigate between splits |
| `Cmd+Shift+1-9` | Switch to window N |
| `Cmd+G` | Open file at line in nvim |
| `Cmd+Q` | Save session and quit |

#### Files

```
kitty/
├── kitty.conf          # Main configuration
├── current-theme.conf  # Catppuccin Mocha theme
├── tab_bar.py          # Custom neon tab bar renderer
└── reset-shell.zsh     # Clean shell state for new tabs
```

## Setup

```bash
# Symlink kitty config
ln -sf $(pwd)/kitty ~/.config/kitty
```

## License

MIT

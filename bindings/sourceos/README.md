# SourceOS / SociOS keyboard contract bindings

This directory records the downstream keyboard-navigation contract binding for `browser-use`.

## Purpose

`browser-use` consumes the shared SourceOS / SociOS interaction canon.
It does not own the canonical keyboard-navigation model.

## Current binding

- `browser-use.interaction-surface.json` — browser-side `InteractionSurface` binding for the browser automation / browser-local interaction surface.
- `browser_use/sourceos_binding.py` — small runtime helper exposing the same surface metadata to Python consumers.

## Placement rule

Canonical schema ownership remains in `SourceOS-Linux/sourceos-spec`.
Browser-side logic binds to that canon downstream.

"""SourceOS / SociOS keyboard-contract binding helpers for browser-use.

This module intentionally stays small. It exposes the browser-side interaction
surface metadata so downstream browser logic can consume the shared keyboard-nav
canon without making `browser-use` the owner of that canon.
"""

from __future__ import annotations

from typing import Any

_INTERACTION_SURFACE: dict[str, Any] = {
    'id': 'urn:srcos:interaction-surface:browser-use',
    'name': 'Browser Use Surface',
    'description': 'Browser automation and browser-local keyboard interaction surface bound to the shared SourceOS/SociOS keyboard-first contracts.',
    'surfaceType': 'browser',
    'platform': 'cross-platform',
    'modalities': ['keyboard', 'pointer', 'hybrid'],
    'focusPolicy': {
        'owner': 'local-surface',
        'escapeBehavior': 'layered-unwind',
        'tabBehavior': 'completion-first',
        'multilineBoundaryHistory': False,
        'arrowKeyPolicy': 'caret-or-local',
    },
    'hostBoundaryPolicy': {
        'nativeShortcutPolicy': 'preserve',
        'passThroughInput': True,
        'protectedNamespaces': ['browser.text-field', 'browser.chrome', 'accessibility'],
    },
    'commandBinding': {
        'defaultInterpretation': 'search',
        'scopePrefix': '/',
        'explicitCommandPrefix': '>',
        'commandBusRef': 'urn:srcos:command-bus:emvi',
        'launcherRef': None,
        'shortcutOverlayRef': None,
        'keymapProfileRef': 'urn:srcos:keymap-profile:mac-linux-primary',
    },
    'evidenceRefs': [],
    'tags': ['browser', 'keyboard-nav', 'sourceos-binding', 'cross-surface'],
}


def get_sourceos_interaction_surface() -> dict[str, Any]:
    """Return the browser-use SourceOS interaction-surface binding.

    This returns a copy so callers can enrich it locally without mutating the
    module-level canonical binding payload.
    """
    return {
        **_INTERACTION_SURFACE,
        'focusPolicy': dict(_INTERACTION_SURFACE['focusPolicy']),
        'hostBoundaryPolicy': dict(_INTERACTION_SURFACE['hostBoundaryPolicy']),
        'commandBinding': dict(_INTERACTION_SURFACE['commandBinding']),
        'modalities': list(_INTERACTION_SURFACE['modalities']),
        'evidenceRefs': list(_INTERACTION_SURFACE['evidenceRefs']),
        'tags': list(_INTERACTION_SURFACE['tags']),
    }

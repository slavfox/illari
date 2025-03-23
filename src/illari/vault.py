# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2025, Slavfox

class Vault:
    """Interface to interacting with an Obsidian vault."""

    def __init__(self, path: str):
        self.path = path

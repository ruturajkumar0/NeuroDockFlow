#!/usr/bin/env python3
"""
NeuroDynamics - Entry point for Molecular Dynamics Analysis Platform
"""

from neurodynamics.app import app

if __name__ == "__main__":
    app.run(
        debug=False,
        host="0.0.0.0",
        port=8502
    )
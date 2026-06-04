#!/usr/bin/env python3
"""
Run the NeuroDynamicsFlow web server.

Usage:
    python -m neurodynamicsflow
    neurodynamicsflow
"""

from neurodynamicsflow.app import app


def main():
    app.run(
        debug=False,
        host="0.0.0.0",
        port=8502
    )


if __name__ == "__main__":
    main()
# GitGraphBot

This repo is designed to populate a user's git graph with with simulated activity.

## Setup & Usage

Clone the repo using `ssh` (using `https` will prevent `cron` from accessing git credentials in many cases).

Run `python3 cron.py` to schedule a daily job that will push commits to this repo at random.

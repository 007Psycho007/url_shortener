#!/bin/bash
cd "$(dirname "$0")"
pip3 install -r ../application/requirements.txt
cp ./url_shortener.service /etc/systemd/system/url_shortener.service


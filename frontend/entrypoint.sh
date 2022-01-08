#!/bin/sh

if [ $TYPE_ENV = "dev" ]; then 
  npm run dev; 
else 
  npm run build; \
  npm run start;
fi
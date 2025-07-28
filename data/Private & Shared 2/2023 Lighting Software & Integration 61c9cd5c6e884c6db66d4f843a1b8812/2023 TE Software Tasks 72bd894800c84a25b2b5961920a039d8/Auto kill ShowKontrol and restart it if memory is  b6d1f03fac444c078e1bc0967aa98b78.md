# Auto kill ShowKontrol and restart it if memory is too high

Assignee: Will Drevo
Created by: Will Drevo
Description: Should be if memory > 15GB or so
Notes: WIP PR here: https://github.com/titanicsend/LXStudio-TE/pull/344 
Priority: P0
Status: In progress

- Dumbest solution: shell script that runs periodically && kill -9 <process-id> && re-runs
- Better solution: beat-link-trigger at San Carlos
- Even better solution: Bring CDJs home & test it
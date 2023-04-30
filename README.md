# tasktual - A TUI App for Taskwarrior
A Python frontend to [Taskwarrior](https://taskwarrior.org) with [textual](https://github.com/textualize/textual/).

## First Draft of the MainScreen

```
  ┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │                                          tasktual - Sunday, 2023-04-16                                    │
  ├────────────────┬──────────────────────────────────────────────────────────────────────────────────────────┤
  │ Dashboard      │Filter:                                                                                   │
  │ ▼ Reports      ├────┬──────────┬──────┬────┬─────────┬───────────┬──────────┬─────────────────────────────┤
  │   ├ Overdue    │ID  │Started   │Active│Age │Project  │Tags       │Due       │Description                  │
  │   ├ Active     ├────┴──────────┴──────┴────┴─────────┴───────────┴──────────┴─────────────────────────────┤
  │   ├ Next       │                                                                                          │
  │   ├ Blocked    │  36 2023-04-15   1d    1h   tasktual coding, wip 2023-04-26 Taskwarrior App with textual │
  │   ├ Blocking   │                                                                                          │
  │   └ Waiting    │                                                                                          │
  │► Projects      │                                                                                          │
  │► Tags          │                                                                                          │
  │                │                                                                                          │
  │                ├──────────────────────────────────────────────────────────────────────────────────────────┤
  │                │Annotations  -  Details                                                                   │
  │                ├──────────────────────────────────────────────────────────────────────────────────────────┤
  │                │ TextName      Value                                                                      │
  │                │ ID            36                                                                         │
  │                │ Description   Taskwarrior App with textual                                               │
  │                │ Status        Pending                                                                    │
  │                │ Project       coding                                                                     │
  │                │ Entered       2023-04-16 08:01:18 (1h)                                                   │
  │                │ Start         2023-04-16 08:02:02                                                        │
  │                │ Due           2023-04-17 00:00:00                                                        │
  │                │ Last modified 2023-04-16 08:08:32 (1h)                                                   │
  │                │ Tags          wip                                                                        │
  │                │ Virtual tags  ACTIVE DUE MONTH PENDING PROJECT QUARTER READY TAGGED TOMORROW             │
  │                │ UNBLOCKED YEAR                                                                           │
  │                │ UUID          9cfb70b4-9bd3-4905-9553-f2c3f0bccc11                                       │
  │                │ Urgency       14.32                                                                      │
  ├────────────────┴──────────────────────────────────────────────────────────────────────────────────────────┤
  │CTRL-C | Quit - CTRL-R | Reload                                                                            │
  └───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
Please stand by ... 😉

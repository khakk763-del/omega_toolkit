# NHTSA complaints vs recalls — 25 best-selling US SUVs and trucks, 2021–2023

Desk log for Synmerco job `job_8ae6039716f24472` (bid 2352, Meridian Risk). Awarded 2026-11-04T12:05:09Z. All data from public NHTSA sources only (vpic.nhtsa.dot.gov and api.nhtsa.gov); no contact with anyone.

## Data files

- `uncovered-pull1.csv` — 1614 rows, SHA-256 `dc196a8ce7b26967b127aae4f509ce750bb95a74a363637bdc324ff8994a3270` (PULL 1, 2026-11-04T12:43:33Z)
- `uncovered-pull2.csv` — pending PULL 2 (about 12 hours after the PULL 1 note).

CSV columns: make, model, model_year, component, complaint_count, recall_count. One row = one component of one vehicle-year that appears in complaints or recalls; an empty source value stays an empty cell.

## 1. Name table

| Vehicle (as listed) | vPIC spelling | NHTSA spelling used | Rejected spelling(s) |
|---|---|---|---|
| Chevrolet Silverado 1500 | Silverado | Silverado 1500 | Silverado |
| Ram 1500 | 1500 | 1500 | — |
| GMC Sierra 1500 | Sierra | Sierra 1500 | Sierra |
| Toyota RAV4 | RAV4 | RAV4 | — |
| Honda CR-V | CR-V | CR-V | — |
| Toyota Camry | Camry | Camry | — |
| Nissan Rogue | Rogue | Rogue | — |
| Chevrolet Equinox | Equinox | Equinox | — |
| Toyota Tacoma | Tacoma | Tacoma | — |
| Honda Civic | Civic | Civic | — |
| Honda Accord | Accord | Accord | — |
| Ford Escape | Escape | Escape | — |
| Toyota Corolla | Corolla | Corolla | — |
| Jeep Grand Cherokee | Grand Cherokee | Grand Cherokee | — |
| Ford Edge | Edge | Edge | — |
| Subaru Forester | Forester | Forester | — |
| Jeep Wrangler | Wrangler | Wrangler | — |
| Toyota Highlander | Highlander | Highlander | — |
| Hyundai Tucson | Tucson | Tucson | — |
| Chevrolet Tahoe | Tahoe | Tahoe | — |
| Honda Pilot | Pilot | Pilot | — |
| Kia Sportage | Sportage | Sportage | — |
| Subaru Outback | Outback | Outback | — |
| Chevrolet Traverse | Traverse | Traverse | — |
| Ford Bronco Sport | Bronco Sport | Bronco Sport | — |

## 2. Vehicle-year counts

| Make | Model | Model year | Complaints (Count) | Recalls (Count) | Status |
|---|---|---|---|---|---|
| Chevrolet | Silverado 1500 | 2021 | 855 | 8 | ok |
| Chevrolet | Silverado 1500 | 2022 | 656 | 6 | ok |
| Chevrolet | Silverado 1500 | 2023 | 391 | 3 | ok |
| Ram | 1500 | 2021 | 686 | 15 | ok |
| Ram | 1500 | 2022 | 0 | 16 | ok |
| Ram | 1500 | 2023 | 0 | 11 | ok |
| GMC | Sierra 1500 | 2021 | 601 | 7 | ok |
| GMC | Sierra 1500 | 2022 | 603 | 6 | ok |
| GMC | Sierra 1500 | 2023 | 507 | 3 | ok |
| Toyota | RAV4 | 2021 | 389 | 1 | ok |
| Toyota | RAV4 | 2022 | 150 | 1 | ok |
| Toyota | RAV4 | 2023 | 164 | 3 | ok |
| Honda | CR-V | 2021 | 341 | 4 | ok |
| Honda | CR-V | 2022 | 269 | 3 | ok |
| Honda | CR-V | 2023 | 517 | 3 | ok |
| Toyota | Camry | 2021 | 158 | 1 | ok |
| Toyota | Camry | 2022 | 65 | 1 | ok |
| Toyota | Camry | 2023 | 65 | 2 | ok |
| Nissan | Rogue | 2021 | 295 | 10 | ok |
| Nissan | Rogue | 2022 | 270 | 6 | ok |
| Nissan | Rogue | 2023 | 766 | 6 | ok |
| Chevrolet | Equinox | 2021 | 100 | 4 | ok |
| Chevrolet | Equinox | 2022 | 183 | 5 | ok |
| Chevrolet | Equinox | 2023 | 99 | 3 | ok |
| Toyota | Tacoma | 2021 | 81 | 0 | ok |
| Toyota | Tacoma | 2022 | 59 | 3 | ok |
| Toyota | Tacoma | 2023 | 54 | 4 | ok |
| Honda | Civic | 2021 | 148 | 4 | ok |
| Honda | Civic | 2022 | 886 | 4 | ok |
| Honda | Civic | 2023 | 0 | 4 | ok |
| Honda | Accord | 2021 | 246 | 4 | ok |
| Honda | Accord | 2022 | 262 | 4 | ok |
| Honda | Accord | 2023 | 0 | 5 | ok |
| Ford | Escape | 2021 | 355 | 19 | ok |
| Ford | Escape | 2022 | 238 | 19 | ok |
| Ford | Escape | 2023 | 102 | 11 | ok |
| Toyota | Corolla | 2021 | 188 | 1 | ok |
| Toyota | Corolla | 2022 | 102 | 0 | ok |
| Toyota | Corolla | 2023 | 74 | 3 | ok |
| Jeep | Grand Cherokee | 2021 | 411 | 12 | ok |
| Jeep | Grand Cherokee | 2022 | 379 | 13 | ok |
| Jeep | Grand Cherokee | 2023 | 408 | 21 | ok |
| Ford | Edge | 2021 | 114 | 7 | ok |
| Ford | Edge | 2022 | 135 | 5 | ok |
| Ford | Edge | 2023 | 23 | 4 | ok |
| Subaru | Forester | 2021 | 215 | 0 | ok |
| Subaru | Forester | 2022 | 100 | 1 | ok |
| Subaru | Forester | 2023 | 74 | 1 | ok |
| Jeep | Wrangler | 2021 | 960 | 15 | ok |
| Jeep | Wrangler | 2022 | 413 | 15 | ok |
| Jeep | Wrangler | 2023 | 376 | 14 | ok |
| Toyota | Highlander | 2021 | 535 | 4 | ok |
| Toyota | Highlander | 2022 | 266 | 5 | ok |
| Toyota | Highlander | 2023 | 189 | 9 | ok |
| Hyundai | Tucson | 2021 | 80 | 1 | ok |
| Hyundai | Tucson | 2022 | 390 | 3 | ok |
| Hyundai | Tucson | 2023 | 136 | 2 | ok |
| Chevrolet | Tahoe | 2021 | 465 | 16 | ok |
| Chevrolet | Tahoe | 2022 | 197 | 4 | ok |
| Chevrolet | Tahoe | 2023 | 234 | 5 | ok |
| Honda | Pilot | 2021 | 454 | 10 | ok |
| Honda | Pilot | 2022 | 174 | 5 | ok |
| Honda | Pilot | 2023 | 149 | 5 | ok |
| Kia | Sportage | 2021 | 54 | 2 | ok |
| Kia | Sportage | 2022 | 47 | 1 | ok |
| Kia | Sportage | 2023 | 196 | 6 | ok |
| Subaru | Outback | 2021 | 299 | 4 | ok |
| Subaru | Outback | 2022 | 465 | 4 | ok |
| Subaru | Outback | 2023 | 89 | 2 | ok |
| Chevrolet | Traverse | 2021 | 94 | 3 | ok |
| Chevrolet | Traverse | 2022 | 103 | 1 | ok |
| Chevrolet | Traverse | 2023 | 95 | 2 | ok |
| Ford | Bronco Sport | 2021 | 713 | 16 | ok |
| Ford | Bronco Sport | 2022 | 370 | 15 | ok |
| Ford | Bronco Sport | 2023 | 163 | 14 | ok |

## 3. Uncovered components (PULL 1)

Uncovered = at least 10 complaints and no recall campaign with that component for that vehicle-year. Two lowest odiNumber values per component.

| Make | Model | Model year | Component | Complaints | odiNumber 1 | odiNumber 2 |
|---|---|---|---|---|---|---|
| Chevrolet | Equinox | 2021 | ELECTRICAL SYSTEM | 18 | 11448338 | 11451627 |
| Chevrolet | Equinox | 2021 | ENGINE | 16 | 11448277 | 11495225 |
| Chevrolet | Equinox | 2021 | FUEL/PROPULSION SYSTEM | 20 | 11506709 | 11552345 |
| Chevrolet | Equinox | 2021 | POWER TRAIN | 17 | 11422780 | 11442734 |
| Chevrolet | Equinox | 2022 | ELECTRICAL SYSTEM | 20 | 11502475 | 11539806 |
| Chevrolet | Equinox | 2022 | ENGINE | 28 | 11454280 | 11502475 |
| Chevrolet | Equinox | 2022 | FUEL/PROPULSION SYSTEM | 80 | 11466225 | 11470022 |
| Chevrolet | Equinox | 2022 | POWER TRAIN | 12 | 11490746 | 11518165 |
| Chevrolet | Equinox | 2023 | ELECTRICAL SYSTEM | 13 | 11509281 | 11551574 |
| Chevrolet | Equinox | 2023 | ENGINE | 18 | 11507636 | 11533070 |
| Chevrolet | Equinox | 2023 | FUEL/PROPULSION SYSTEM | 46 | 11558232 | 11564698 |
| Chevrolet | Equinox | 2023 | SERVICE BRAKES | 14 | 11503877 | 11531937 |
| Chevrolet | Silverado 1500 | 2021 | ELECTRICAL SYSTEM | 113 | 11384725 | 11385179 |
| Chevrolet | Silverado 1500 | 2021 | ENGINE | 396 | 11384725 | 11397267 |
| Chevrolet | Silverado 1500 | 2021 | FORWARD COLLISION AVOIDANCE | 10 | 11590938 | 11636290 |
| Chevrolet | Silverado 1500 | 2021 | FUEL/PROPULSION SYSTEM | 30 | 11397267 | 11456398 |
| Chevrolet | Silverado 1500 | 2021 | LATCHES/LOCKS/LINKAGES | 15 | 11521043 | 11579583 |
| Chevrolet | Silverado 1500 | 2021 | SERVICE BRAKES | 40 | 11414715 | 11415357 |
| Chevrolet | Silverado 1500 | 2021 | STEERING | 43 | 11406248 | 11415357 |
| Chevrolet | Silverado 1500 | 2021 | STRUCTURE | 29 | 11399837 | 11423153 |
| Chevrolet | Silverado 1500 | 2021 | SUSPENSION | 18 | 11390737 | 11403831 |
| Chevrolet | Silverado 1500 | 2021 | VEHICLE SPEED CONTROL | 10 | 11383190 | 11519627 |
| Chevrolet | Silverado 1500 | 2022 | BACK OVER PREVENTION | 13 | 11495848 | 11503189 |
| Chevrolet | Silverado 1500 | 2022 | ELECTRICAL SYSTEM | 140 | 11464650 | 11466968 |
| Chevrolet | Silverado 1500 | 2022 | ENGINE | 257 | 11456587 | 11456822 |
| Chevrolet | Silverado 1500 | 2022 | FORWARD COLLISION AVOIDANCE | 29 | 11479583 | 11486547 |
| Chevrolet | Silverado 1500 | 2022 | FUEL/PROPULSION SYSTEM | 43 | 11464650 | 11497929 |
| Chevrolet | Silverado 1500 | 2022 | LANE DEPARTURE | 15 | 11530045 | 11653833 |
| Chevrolet | Silverado 1500 | 2022 | LATCHES/LOCKS/LINKAGES | 12 | 11617853 | 11646677 |
| Chevrolet | Silverado 1500 | 2022 | SERVICE BRAKES | 55 | 11476450 | 11486784 |
| Chevrolet | Silverado 1500 | 2022 | STEERING | 15 | 11476450 | 11501753 |
| Chevrolet | Silverado 1500 | 2022 | STRUCTURE | 13 | 11486187 | 11534590 |
| Chevrolet | Silverado 1500 | 2022 | VEHICLE SPEED CONTROL | 12 | 11514910 | 11556514 |
| Chevrolet | Silverado 1500 | 2023 | ELECTRICAL SYSTEM | 63 | 11507327 | 11528583 |
| Chevrolet | Silverado 1500 | 2023 | ENGINE | 153 | 11522975 | 11552032 |
| Chevrolet | Silverado 1500 | 2023 | FORWARD COLLISION AVOIDANCE | 21 | 11507710 | 11540577 |
| Chevrolet | Silverado 1500 | 2023 | FUEL/PROPULSION SYSTEM | 33 | 11510069 | 11542689 |
| Chevrolet | Silverado 1500 | 2023 | POWER TRAIN | 108 | 11514463 | 11542689 |
| Chevrolet | Silverado 1500 | 2023 | SERVICE BRAKES | 18 | 11507327 | 11507710 |
| Chevrolet | Silverado 1500 | 2023 | VEHICLE SPEED CONTROL | 18 | 11507327 | 11507710 |
| Chevrolet | Tahoe | 2021 | ELECTRICAL SYSTEM | 58 | 11361893 | 11378279 |
| Chevrolet | Tahoe | 2021 | ENGINE | 171 | 11378279 | 11384381 |
| Chevrolet | Tahoe | 2021 | FORWARD COLLISION AVOIDANCE | 21 | 11397468 | 11418385 |
| Chevrolet | Tahoe | 2021 | FUEL/PROPULSION SYSTEM | 96 | 11418949 | 11421145 |
| Chevrolet | Tahoe | 2021 | SERVICE BRAKES | 19 | 11372952 | 11452857 |
| Chevrolet | Tahoe | 2021 | VEHICLE SPEED CONTROL | 10 | 11483330 | 11486412 |
| Chevrolet | Tahoe | 2022 | ELECTRICAL SYSTEM | 38 | 11444994 | 11477442 |
| Chevrolet | Tahoe | 2022 | ENGINE | 75 | 11458077 | 11503084 |
| Chevrolet | Tahoe | 2022 | FUEL/PROPULSION SYSTEM | 20 | 11542219 | 11570893 |
| Chevrolet | Tahoe | 2022 | SERVICE BRAKES | 12 | 11447884 | 11494644 |
| Chevrolet | Tahoe | 2023 | ELECTRICAL SYSTEM | 40 | 11507123 | 11523171 |
| Chevrolet | Tahoe | 2023 | ENGINE | 128 | 11545614 | 11562182 |
| Chevrolet | Tahoe | 2023 | FORWARD COLLISION AVOIDANCE | 12 | 11602977 | 11627195 |
| Chevrolet | Tahoe | 2023 | FUEL/PROPULSION SYSTEM | 14 | 11570874 | 11589616 |
| Chevrolet | Tahoe | 2023 | POWER TRAIN | 47 | 11547936 | 11560962 |
| Chevrolet | Tahoe | 2023 | SERVICE BRAKES | 21 | 11560962 | 11580791 |
| Chevrolet | Traverse | 2021 | ELECTRICAL SYSTEM | 22 | 11449517 | 11518119 |
| Chevrolet | Traverse | 2021 | ENGINE | 11 | 11441316 | 11506571 |
| Chevrolet | Traverse | 2021 | SERVICE BRAKES | 10 | 11415778 | 11416250 |
| Chevrolet | Traverse | 2022 | ELECTRICAL SYSTEM | 18 | 11499709 | 11516420 |
| Chevrolet | Traverse | 2022 | ENGINE | 18 | 11462661 | 11485418 |
| Chevrolet | Traverse | 2022 | POWER TRAIN | 45 | 11509971 | 11531171 |
| Chevrolet | Traverse | 2023 | ELECTRICAL SYSTEM | 21 | 11532899 | 11539607 |
| Chevrolet | Traverse | 2023 | ENGINE | 19 | 11532899 | 11567972 |
| Chevrolet | Traverse | 2023 | SERVICE BRAKES | 12 | 11555218 | 11604400 |
| Ford | Bronco Sport | 2021 | ENGINE | 152 | 11448393 | 11448737 |
| Ford | Bronco Sport | 2021 | EXTERIOR LIGHTING | 10 | 11446958 | 11473343 |
| Ford | Bronco Sport | 2021 | FORWARD COLLISION AVOIDANCE | 15 | 11413559 | 11449342 |
| Ford | Bronco Sport | 2021 | FUEL/PROPULSION SYSTEM | 64 | 11443569 | 11454100 |
| Ford | Bronco Sport | 2021 | SERVICE BRAKES | 101 | 11442253 | 11447244 |
| Ford | Bronco Sport | 2021 | STEERING | 16 | 11511567 | 11584190 |
| Ford | Bronco Sport | 2021 | VEHICLE SPEED CONTROL | 13 | 11481549 | 11497354 |
| Ford | Bronco Sport | 2021 | VISIBILITY/WIPER | 11 | 11423365 | 11427514 |
| Ford | Bronco Sport | 2022 | ENGINE | 83 | 11452595 | 11462833 |
| Ford | Bronco Sport | 2022 | FORWARD COLLISION AVOIDANCE | 15 | 11462723 | 11508539 |
| Ford | Bronco Sport | 2022 | FUEL/PROPULSION SYSTEM | 43 | 11474812 | 11475881 |
| Ford | Bronco Sport | 2022 | SERVICE BRAKES | 44 | 11462833 | 11463713 |
| Ford | Bronco Sport | 2022 | STEERING | 14 | 11476738 | 11494193 |
| Ford | Bronco Sport | 2022 | VEHICLE SPEED CONTROL | 10 | 11544687 | 11567727 |
| Ford | Bronco Sport | 2023 | ENGINE | 38 | 11540264 | 11544418 |
| Ford | Bronco Sport | 2023 | FUEL/PROPULSION SYSTEM | 29 | 11566060 | 11566257 |
| Ford | Edge | 2021 | ELECTRICAL SYSTEM | 14 | 11423419 | 11470584 |
| Ford | Edge | 2021 | ENGINE | 11 | 11476580 | 11569903 |
| Ford | Edge | 2022 | ELECTRICAL SYSTEM | 18 | 11485911 | 11487379 |
| Ford | Edge | 2022 | ENGINE | 13 | 11497388 | 11509712 |
| Ford | Edge | 2022 | POWER TRAIN | 47 | 11564102 | 11588019 |
| Ford | Escape | 2021 | FUEL/PROPULSION SYSTEM | 29 | 11426742 | 11447232 |
| Ford | Escape | 2021 | SERVICE BRAKES | 40 | 11442905 | 11444169 |
| Ford | Escape | 2022 | FUEL/PROPULSION SYSTEM | 24 | 11629080 | 11632660 |
| Ford | Escape | 2022 | SERVICE BRAKES | 33 | 11466339 | 11486242 |
| Ford | Escape | 2023 | POWER TRAIN | 25 | 11552516 | 11571481 |
| GMC | Sierra 1500 | 2021 | ELECTRICAL SYSTEM | 76 | 11378394 | 11408633 |
| GMC | Sierra 1500 | 2021 | ENGINE | 324 | 11383585 | 11396897 |
| GMC | Sierra 1500 | 2021 | FUEL/PROPULSION SYSTEM | 41 | 11396897 | 11431331 |
| GMC | Sierra 1500 | 2021 | LATCHES/LOCKS/LINKAGES | 10 | 11595515 | 11602610 |
| GMC | Sierra 1500 | 2021 | SERVICE BRAKES | 24 | 11378394 | 11430809 |
| GMC | Sierra 1500 | 2021 | STEERING | 35 | 11378394 | 11388759 |
| GMC | Sierra 1500 | 2021 | STRUCTURE | 13 | 11415136 | 11423289 |
| GMC | Sierra 1500 | 2021 | SUSPENSION | 10 | 11430578 | 11479962 |
| GMC | Sierra 1500 | 2022 | ELECTRICAL SYSTEM | 83 | 11458511 | 11462350 |
| GMC | Sierra 1500 | 2022 | ENGINE | 241 | 11458165 | 11460502 |
| GMC | Sierra 1500 | 2022 | FORWARD COLLISION AVOIDANCE | 24 | 11458511 | 11470390 |
| GMC | Sierra 1500 | 2022 | FUEL/PROPULSION SYSTEM | 29 | 11507349 | 11609069 |
| GMC | Sierra 1500 | 2022 | LANE DEPARTURE | 13 | 11452251 | 11470390 |
| GMC | Sierra 1500 | 2022 | SERVICE BRAKES | 28 | 11458165 | 11458511 |
| GMC | Sierra 1500 | 2022 | STEERING | 13 | 11491138 | 11497631 |
| GMC | Sierra 1500 | 2023 | ELECTRICAL SYSTEM | 64 | 11506426 | 11531556 |
| GMC | Sierra 1500 | 2023 | ENGINE | 214 | 11508802 | 11524059 |
| GMC | Sierra 1500 | 2023 | FORWARD COLLISION AVOIDANCE | 14 | 11544881 | 11545089 |
| GMC | Sierra 1500 | 2023 | FUEL/PROPULSION SYSTEM | 37 | 11513606 | 11566879 |
| GMC | Sierra 1500 | 2023 | POWER TRAIN | 92 | 11558187 | 11566879 |
| GMC | Sierra 1500 | 2023 | SERVICE BRAKES | 14 | 11541322 | 11545089 |
| GMC | Sierra 1500 | 2023 | STEERING | 13 | 11539087 | 11565685 |
| GMC | Sierra 1500 | 2023 | STRUCTURE | 95 | 11531780 | 11542786 |
| GMC | Sierra 1500 | 2023 | VEHICLE SPEED CONTROL | 11 | 11524059 | 11545089 |
| Honda | Accord | 2021 | ELECTRICAL SYSTEM | 68 | 11453797 | 11455604 |
| Honda | Accord | 2021 | ENGINE | 39 | 11434291 | 11539109 |
| Honda | Accord | 2021 | FORWARD COLLISION AVOIDANCE | 62 | 11435932 | 11453797 |
| Honda | Accord | 2021 | FUEL/PROPULSION SYSTEM | 14 | 11625538 | 11641004 |
| Honda | Accord | 2021 | LANE DEPARTURE | 16 | 11440569 | 11457907 |
| Honda | Accord | 2021 | POWER TRAIN | 14 | 11431095 | 11482521 |
| Honda | Accord | 2021 | SERVICE BRAKES | 29 | 11412992 | 11446693 |
| Honda | Accord | 2022 | ELECTRICAL SYSTEM | 108 | 11470005 | 11481470 |
| Honda | Accord | 2022 | ENGINE | 32 | 11442409 | 11470005 |
| Honda | Accord | 2022 | FORWARD COLLISION AVOIDANCE | 61 | 11454059 | 11473060 |
| Honda | Accord | 2022 | FUEL/PROPULSION SYSTEM | 17 | 11550704 | 11615703 |
| Honda | Accord | 2022 | LANE DEPARTURE | 12 | 11473060 | 11485607 |
| Honda | Accord | 2022 | SERVICE BRAKES | 17 | 11454059 | 11470005 |
| Honda | Accord | 2022 | STEERING | 14 | 11461404 | 11569759 |
| Honda | Accord | 2022 | VEHICLE SPEED CONTROL | 11 | 11516373 | 11517902 |
| Honda | CR-V | 2021 | ELECTRICAL SYSTEM | 34 | 11399794 | 11423593 |
| Honda | CR-V | 2021 | ENGINE | 33 | 11402938 | 11497396 |
| Honda | CR-V | 2021 | FORWARD COLLISION AVOIDANCE | 89 | 11427130 | 11435201 |
| Honda | CR-V | 2021 | FUEL/PROPULSION SYSTEM | 27 | 11402938 | 11532692 |
| Honda | CR-V | 2021 | LANE DEPARTURE | 17 | 11454419 | 11458287 |
| Honda | CR-V | 2021 | POWER TRAIN | 12 | 11402938 | 11461799 |
| Honda | CR-V | 2021 | SERVICE BRAKES | 26 | 11399794 | 11419870 |
| Honda | CR-V | 2021 | STEERING | 116 | 11415033 | 11514810 |
| Honda | CR-V | 2021 | VISIBILITY/WIPER | 10 | 11452500 | 11456449 |
| Honda | CR-V | 2022 | ELECTRICAL SYSTEM | 14 | 11468645 | 11548515 |
| Honda | CR-V | 2022 | ENGINE | 19 | 11491591 | 11510566 |
| Honda | CR-V | 2022 | FORWARD COLLISION AVOIDANCE | 44 | 11454061 | 11456239 |
| Honda | CR-V | 2022 | LANE DEPARTURE | 12 | 11456239 | 11472619 |
| Honda | CR-V | 2022 | POWER TRAIN | 10 | 11470940 | 11480060 |
| Honda | CR-V | 2022 | SERVICE BRAKES | 14 | 11515808 | 11553920 |
| Honda | CR-V | 2022 | STEERING | 143 | 11456239 | 11559985 |
| Honda | CR-V | 2023 | ELECTRICAL SYSTEM | 28 | 11509741 | 11522659 |
| Honda | CR-V | 2023 | ENGINE | 21 | 11530531 | 11531924 |
| Honda | CR-V | 2023 | FORWARD COLLISION AVOIDANCE | 38 | 11513135 | 11513722 |
| Honda | CR-V | 2023 | FUEL/PROPULSION SYSTEM | 16 | 11559520 | 11593773 |
| Honda | CR-V | 2023 | LANE DEPARTURE | 30 | 11513135 | 11528730 |
| Honda | CR-V | 2023 | POWER TRAIN | 14 | 11530531 | 11568162 |
| Honda | CR-V | 2023 | SERVICE BRAKES | 29 | 11520655 | 11531369 |
| Honda | CR-V | 2023 | STRUCTURE | 23 | 11525798 | 11526919 |
| Honda | CR-V | 2023 | VEHICLE SPEED CONTROL | 13 | 11514771 | 11520655 |
| Honda | CR-V | 2023 | VISIBILITY/WIPER | 25 | 11530036 | 11530558 |
| Honda | Civic | 2021 | ELECTRICAL SYSTEM | 18 | 11400071 | 11419733 |
| Honda | Civic | 2021 | FORWARD COLLISION AVOIDANCE | 33 | 11454186 | 11454439 |
| Honda | Civic | 2021 | LANE DEPARTURE | 11 | 11468518 | 11468636 |
| Honda | Civic | 2021 | SERVICE BRAKES | 17 | 11440302 | 11461876 |
| Honda | Civic | 2021 | STEERING | 67 | 11471885 | 11485983 |
| Honda | Civic | 2022 | ELECTRICAL SYSTEM | 38 | 11426529 | 11432628 |
| Honda | Civic | 2022 | ENGINE | 11 | 11432628 | 11465238 |
| Honda | Civic | 2022 | FORWARD COLLISION AVOIDANCE | 71 | 11442415 | 11444978 |
| Honda | Civic | 2022 | LANE DEPARTURE | 66 | 11452206 | 11456417 |
| Honda | Civic | 2022 | POWER TRAIN | 10 | 11532207 | 11544007 |
| Honda | Civic | 2022 | SERVICE BRAKES | 23 | 11448230 | 11454033 |
| Honda | Civic | 2022 | STRUCTURE | 13 | 11439718 | 11475532 |
| Honda | Civic | 2022 | SUSPENSION | 25 | 11452206 | 11487303 |
| Honda | Civic | 2022 | VEHICLE SPEED CONTROL | 42 | 11442415 | 11444978 |
| Honda | Civic | 2022 | VISIBILITY/WIPER | 12 | 11450545 | 11456417 |
| Honda | Civic | 2022 | WHEELS | 14 | 11526017 | 11555777 |
| Honda | Pilot | 2021 | ENGINE | 113 | 11418420 | 11435014 |
| Honda | Pilot | 2021 | FORWARD COLLISION AVOIDANCE | 99 | 11427520 | 11432266 |
| Honda | Pilot | 2021 | FUEL/PROPULSION SYSTEM | 23 | 11485033 | 11539644 |
| Honda | Pilot | 2021 | LANE DEPARTURE | 45 | 11421911 | 11522826 |
| Honda | Pilot | 2021 | POWER TRAIN | 25 | 11407317 | 11438405 |
| Honda | Pilot | 2021 | SERVICE BRAKES | 26 | 11440032 | 11453811 |
| Honda | Pilot | 2021 | VISIBILITY/WIPER | 21 | 11390642 | 11425223 |
| Honda | Pilot | 2022 | ELECTRICAL SYSTEM | 41 | 11470449 | 11484965 |
| Honda | Pilot | 2022 | ENGINE | 36 | 11461859 | 11466330 |
| Honda | Pilot | 2022 | FORWARD COLLISION AVOIDANCE | 46 | 11466329 | 11474902 |
| Honda | Pilot | 2022 | LANE DEPARTURE | 20 | 11570788 | 11632768 |
| Honda | Pilot | 2022 | POWER TRAIN | 18 | 11461859 | 11466330 |
| Honda | Pilot | 2022 | SERVICE BRAKES | 17 | 11448719 | 11454041 |
| Honda | Pilot | 2022 | VEHICLE SPEED CONTROL | 11 | 11461859 | 11574517 |
| Honda | Pilot | 2023 | ELECTRICAL SYSTEM | 28 | 11522984 | 11523249 |
| Honda | Pilot | 2023 | ENGINE | 13 | 11538794 | 11540182 |
| Honda | Pilot | 2023 | FORWARD COLLISION AVOIDANCE | 20 | 11531019 | 11553929 |
| Honda | Pilot | 2023 | POWER TRAIN | 10 | 11530533 | 11531018 |
| Honda | Pilot | 2023 | SEAT BELTS | 37 | 11585923 | 11587203 |
| Honda | Pilot | 2023 | SERVICE BRAKES | 17 | 11531832 | 11540182 |
| Hyundai | Tucson | 2021 | ELECTRICAL SYSTEM | 12 | 11387555 | 11402935 |
| Hyundai | Tucson | 2021 | ENGINE | 39 | 11398545 | 11413920 |
| Hyundai | Tucson | 2022 | AIR BAGS | 12 | 11438850 | 11467157 |
| Hyundai | Tucson | 2022 | ENGINE | 116 | 11427751 | 11432538 |
| Hyundai | Tucson | 2022 | FORWARD COLLISION AVOIDANCE | 39 | 11478201 | 11481029 |
| Hyundai | Tucson | 2022 | FUEL/PROPULSION SYSTEM | 132 | 11482099 | 11491205 |
| Hyundai | Tucson | 2022 | POWER TRAIN | 64 | 11421833 | 11424945 |
| Hyundai | Tucson | 2022 | SERVICE BRAKES | 32 | 11454849 | 11481029 |
| Hyundai | Tucson | 2022 | VEHICLE SPEED CONTROL | 14 | 11444744 | 11491807 |
| Hyundai | Tucson | 2023 | ELECTRICAL SYSTEM | 27 | 11498564 | 11503054 |
| Hyundai | Tucson | 2023 | ENGINE | 23 | 11498058 | 11512773 |
| Hyundai | Tucson | 2023 | FORWARD COLLISION AVOIDANCE | 28 | 11499276 | 11517285 |
| Hyundai | Tucson | 2023 | FUEL/PROPULSION SYSTEM | 18 | 11536810 | 11550029 |
| Hyundai | Tucson | 2023 | SERVICE BRAKES | 16 | 11503335 | 11504822 |
| Hyundai | Tucson | 2023 | VEHICLE SPEED CONTROL | 17 | 11504822 | 11512773 |
| Jeep | Grand Cherokee | 2021 | ELECTRICAL SYSTEM | 115 | 11413752 | 11418354 |
| Jeep | Grand Cherokee | 2021 | ENGINE | 61 | 11376781 | 11377744 |
| Jeep | Grand Cherokee | 2021 | FORWARD COLLISION AVOIDANCE | 25 | 11436393 | 11446947 |
| Jeep | Grand Cherokee | 2021 | FUEL/PROPULSION SYSTEM | 40 | 11376781 | 11413752 |
| Jeep | Grand Cherokee | 2021 | LANE DEPARTURE | 29 | 11435754 | 11444464 |
| Jeep | Grand Cherokee | 2021 | POWER TRAIN | 60 | 11399189 | 11423564 |
| Jeep | Grand Cherokee | 2021 | SERVICE BRAKES | 29 | 11395797 | 11414211 |
| Jeep | Grand Cherokee | 2021 | VEHICLE SPEED CONTROL | 17 | 11432989 | 11435373 |
| Jeep | Grand Cherokee | 2022 | ENGINE | 71 | 11470983 | 11472078 |
| Jeep | Grand Cherokee | 2022 | FORWARD COLLISION AVOIDANCE | 65 | 11462648 | 11464616 |
| Jeep | Grand Cherokee | 2022 | FUEL/PROPULSION SYSTEM | 54 | 11516050 | 11563416 |
| Jeep | Grand Cherokee | 2022 | LANE DEPARTURE | 18 | 11457671 | 11463139 |
| Jeep | Grand Cherokee | 2022 | SEATS | 12 | 11469126 | 11647852 |
| Jeep | Grand Cherokee | 2022 | SERVICE BRAKES | 22 | 11472258 | 11482454 |
| Jeep | Grand Cherokee | 2022 | STEERING | 46 | 11456693 | 11463139 |
| Jeep | Grand Cherokee | 2022 | VEHICLE SPEED CONTROL | 20 | 11513357 | 11522222 |
| Jeep | Grand Cherokee | 2023 | ENGINE | 86 | 11503558 | 11523782 |
| Jeep | Grand Cherokee | 2023 | FORWARD COLLISION AVOIDANCE | 40 | 11507874 | 11512274 |
| Jeep | Grand Cherokee | 2023 | FUEL/PROPULSION SYSTEM | 55 | 11535615 | 11538463 |
| Jeep | Grand Cherokee | 2023 | LANE DEPARTURE | 16 | 11518169 | 11519582 |
| Jeep | Grand Cherokee | 2023 | SERVICE BRAKES | 22 | 11519297 | 11519917 |
| Jeep | Grand Cherokee | 2023 | STRUCTURE | 10 | 11514912 | 11542034 |
| Jeep | Grand Cherokee | 2023 | VEHICLE SPEED CONTROL | 18 | 11525952 | 11535259 |
| Jeep | Wrangler | 2021 | AIR BAGS | 10 | 11404746 | 11418297 |
| Jeep | Wrangler | 2021 | FORWARD COLLISION AVOIDANCE | 16 | 11440822 | 11463494 |
| Jeep | Wrangler | 2021 | FUEL/PROPULSION SYSTEM | 116 | 11427635 | 11428459 |
| Jeep | Wrangler | 2021 | SERVICE BRAKES | 24 | 11416684 | 11433716 |
| Jeep | Wrangler | 2021 | SUSPENSION | 181 | 11398971 | 11437481 |
| Jeep | Wrangler | 2021 | VEHICLE SPEED CONTROL | 48 | 11418297 | 11419328 |
| Jeep | Wrangler | 2021 | VISIBILITY/WIPER | 15 | 11384913 | 11390573 |
| Jeep | Wrangler | 2021 | WHEELS | 23 | 11398971 | 11403621 |
| Jeep | Wrangler | 2022 | FUEL/PROPULSION SYSTEM | 66 | 11457580 | 11477003 |
| Jeep | Wrangler | 2022 | SERVICE BRAKES | 13 | 11457504 | 11483959 |
| Jeep | Wrangler | 2022 | SUSPENSION | 60 | 11455370 | 11490125 |
| Jeep | Wrangler | 2022 | VEHICLE SPEED CONTROL | 23 | 11465657 | 11483179 |
| Jeep | Wrangler | 2023 | FUEL/PROPULSION SYSTEM | 66 | 11518374 | 11519606 |
| Jeep | Wrangler | 2023 | SUSPENSION | 39 | 11514223 | 11515738 |
| Jeep | Wrangler | 2023 | VEHICLE SPEED CONTROL | 22 | 11529709 | 11530457 |
| Kia | Sportage | 2021 | ENGINE | 23 | 11448187 | 11496058 |
| Kia | Sportage | 2022 | ENGINE | 22 | 11460241 | 11468689 |
| Kia | Sportage | 2023 | BACK OVER PREVENTION | 11 | 11525911 | 11526134 |
| Kia | Sportage | 2023 | ENGINE | 39 | 11483904 | 11501842 |
| Kia | Sportage | 2023 | FORWARD COLLISION AVOIDANCE | 24 | 11491449 | 11496407 |
| Kia | Sportage | 2023 | FUEL/PROPULSION SYSTEM | 12 | 11511112 | 11523054 |
| Kia | Sportage | 2023 | SERVICE BRAKES | 30 | 11521104 | 11525243 |
| Kia | Sportage | 2023 | VEHICLE SPEED CONTROL | 10 | 11502359 | 11511112 |
| Nissan | Rogue | 2021 | AIR BAGS | 15 | 11424722 | 11459962 |
| Nissan | Rogue | 2021 | ELECTRICAL SYSTEM | 62 | 11406842 | 11424662 |
| Nissan | Rogue | 2021 | ENGINE | 54 | 11398240 | 11408195 |
| Nissan | Rogue | 2021 | FORWARD COLLISION AVOIDANCE | 29 | 11397015 | 11428228 |
| Nissan | Rogue | 2021 | FUEL/PROPULSION SYSTEM | 33 | 11413335 | 11424662 |
| Nissan | Rogue | 2021 | POWER TRAIN | 27 | 11391180 | 11426108 |
| Nissan | Rogue | 2021 | SERVICE BRAKES | 14 | 11406842 | 11477566 |
| Nissan | Rogue | 2021 | STEERING | 18 | 11440734 | 11511431 |
| Nissan | Rogue | 2021 | STRUCTURE | 19 | 11422053 | 11430573 |
| Nissan | Rogue | 2021 | VEHICLE SPEED CONTROL | 11 | 11433356 | 11437256 |
| Nissan | Rogue | 2022 | ELECTRICAL SYSTEM | 22 | 11506081 | 11584869 |
| Nissan | Rogue | 2022 | ENGINE | 147 | 11502315 | 11504489 |
| Nissan | Rogue | 2022 | FUEL/PROPULSION SYSTEM | 47 | 11496829 | 11499442 |
| Nissan | Rogue | 2022 | POWER TRAIN | 41 | 11509261 | 11565870 |
| Nissan | Rogue | 2022 | VEHICLE SPEED CONTROL | 17 | 11509261 | 11522243 |
| Nissan | Rogue | 2023 | ELECTRICAL SYSTEM | 60 | 11516547 | 11535285 |
| Nissan | Rogue | 2023 | ENGINE | 309 | 11500268 | 11501676 |
| Nissan | Rogue | 2023 | FORWARD COLLISION AVOIDANCE | 54 | 11496496 | 11515469 |
| Nissan | Rogue | 2023 | FUEL SYSTEM, GASOLINE | 10 | 11500268 | 11506004 |
| Nissan | Rogue | 2023 | FUEL/PROPULSION SYSTEM | 100 | 11498633 | 11501676 |
| Nissan | Rogue | 2023 | POWER TRAIN | 90 | 11503277 | 11505088 |
| Nissan | Rogue | 2023 | SERVICE BRAKES | 17 | 11496496 | 11507442 |
| Nissan | Rogue | 2023 | STRUCTURE | 14 | 11585097 | 11620716 |
| Nissan | Rogue | 2023 | VEHICLE SPEED CONTROL | 41 | 11528354 | 11541261 |
| Nissan | Rogue | 2023 | VISIBILITY | 26 | 11573443 | 11616353 |
| Nissan | Rogue | 2023 | VISIBILITY/WIPER | 38 | 11621903 | 11622610 |
| Ram | 1500 | 2021 | ELECTRICAL SYSTEM | 199 | 11383816 | 11394690 |
| Ram | 1500 | 2021 | ELECTRONIC STABILITY CONTROL (ESC) | 16 | 11537134 | 11614922 |
| Ram | 1500 | 2021 | ENGINE | 277 | 11406417 | 11406813 |
| Ram | 1500 | 2021 | EXTERIOR LIGHTING | 13 | 11375264 | 11446345 |
| Ram | 1500 | 2021 | FORWARD COLLISION AVOIDANCE | 52 | 11416441 | 11418807 |
| Ram | 1500 | 2021 | FUEL/PROPULSION SYSTEM | 70 | 11391192 | 11406813 |
| Ram | 1500 | 2021 | SERVICE BRAKES | 54 | 11394690 | 11413419 |
| Ram | 1500 | 2021 | STEERING | 50 | 11397445 | 11408038 |
| Ram | 1500 | 2021 | VEHICLE SPEED CONTROL | 30 | 11406813 | 11413950 |
| Ram | 1500 | 2021 | VISIBILITY/WIPER | 20 | 11390974 | 11408080 |
| Subaru | Forester | 2021 | ELECTRICAL SYSTEM | 35 | 11395055 | 11406803 |
| Subaru | Forester | 2021 | ENGINE | 36 | 11440297 | 11462054 |
| Subaru | Forester | 2021 | FORWARD COLLISION AVOIDANCE | 17 | 11433404 | 11438070 |
| Subaru | Forester | 2021 | POWER TRAIN | 17 | 11440297 | 11462054 |
| Subaru | Forester | 2021 | VEHICLE SPEED CONTROL | 12 | 11406235 | 11469925 |
| Subaru | Forester | 2021 | VISIBILITY | 14 | 11414616 | 11415990 |
| Subaru | Forester | 2021 | VISIBILITY/WIPER | 76 | 11389145 | 11396102 |
| Subaru | Forester | 2022 | ELECTRICAL SYSTEM | 11 | 11479790 | 11484729 |
| Subaru | Forester | 2022 | ENGINE | 11 | 11479790 | 11484729 |
| Subaru | Forester | 2022 | FORWARD COLLISION AVOIDANCE | 15 | 11475307 | 11482220 |
| Subaru | Forester | 2022 | SERVICE BRAKES | 11 | 11497153 | 11500187 |
| Subaru | Forester | 2022 | VISIBILITY/WIPER | 20 | 11454529 | 11465227 |
| Subaru | Forester | 2023 | FORWARD COLLISION AVOIDANCE | 13 | 11523158 | 11552427 |
| Subaru | Forester | 2023 | VISIBILITY/WIPER | 11 | 11522557 | 11530644 |
| Subaru | Outback | 2021 | ELECTRICAL SYSTEM | 76 | 11396114 | 11403232 |
| Subaru | Outback | 2021 | ENGINE | 21 | 11432757 | 11433407 |
| Subaru | Outback | 2021 | FORWARD COLLISION AVOIDANCE | 29 | 11375885 | 11383649 |
| Subaru | Outback | 2021 | FUEL/PROPULSION SYSTEM | 10 | 11431728 | 11466335 |
| Subaru | Outback | 2021 | VEHICLE SPEED CONTROL | 19 | 11421481 | 11436737 |
| Subaru | Outback | 2021 | VISIBILITY | 10 | 11383520 | 11398015 |
| Subaru | Outback | 2021 | VISIBILITY/WIPER | 98 | 11375885 | 11383649 |
| Subaru | Outback | 2022 | ELECTRICAL SYSTEM | 52 | 11424796 | 11426401 |
| Subaru | Outback | 2022 | ENGINE | 23 | 11429109 | 11504271 |
| Subaru | Outback | 2022 | FORWARD COLLISION AVOIDANCE | 23 | 11459231 | 11471358 |
| Subaru | Outback | 2022 | LANE DEPARTURE | 11 | 11433231 | 11471358 |
| Subaru | Outback | 2022 | SERVICE BRAKES | 10 | 11450896 | 11474100 |
| Subaru | Outback | 2022 | VISIBILITY/WIPER | 255 | 11429098 | 11436546 |
| Subaru | Outback | 2023 | ELECTRICAL SYSTEM | 17 | 11488010 | 11492069 |
| Subaru | Outback | 2023 | FORWARD COLLISION AVOIDANCE | 22 | 11500283 | 11511110 |
| Subaru | Outback | 2023 | VISIBILITY/WIPER | 16 | 11514367 | 11515781 |
| Toyota | Camry | 2021 | FORWARD COLLISION AVOIDANCE | 10 | 11445902 | 11457038 |
| Toyota | Camry | 2021 | POWER TRAIN | 12 | 11461190 | 11470895 |
| Toyota | Camry | 2021 | SERVICE BRAKES | 13 | 11446379 | 11451933 |
| Toyota | Corolla | 2021 | ELECTRICAL SYSTEM | 23 | 11399776 | 11435034 |
| Toyota | Corolla | 2021 | ENGINE | 41 | 11399776 | 11435034 |
| Toyota | Corolla | 2021 | POWER TRAIN | 19 | 11445388 | 11473590 |
| Toyota | Corolla | 2021 | VISIBILITY/WIPER | 15 | 11433453 | 11445594 |
| Toyota | Corolla | 2022 | AIR BAGS | 10 | 11435361 | 11449309 |
| Toyota | Corolla | 2022 | ELECTRICAL SYSTEM | 21 | 11466503 | 11474560 |
| Toyota | Corolla | 2022 | ENGINE | 14 | 11501798 | 11507910 |
| Toyota | Corolla | 2022 | POWER TRAIN | 17 | 11474625 | 11511343 |
| Toyota | Corolla | 2022 | SERVICE BRAKES | 12 | 11463430 | 11477942 |
| Toyota | Corolla | 2023 | ELECTRICAL SYSTEM | 14 | 11507634 | 11508173 |
| Toyota | Corolla | 2023 | ENGINE | 13 | 11507367 | 11507382 |
| Toyota | Corolla | 2023 | EXTERIOR LIGHTING | 11 | 11510792 | 11523079 |
| Toyota | Highlander | 2021 | ELECTRICAL SYSTEM | 28 | 11418965 | 11442920 |
| Toyota | Highlander | 2021 | ENGINE | 47 | 11416030 | 11417767 |
| Toyota | Highlander | 2021 | FORWARD COLLISION AVOIDANCE | 12 | 11406776 | 11444627 |
| Toyota | Highlander | 2021 | FUEL/PROPULSION SYSTEM | 31 | 11389811 | 11395869 |
| Toyota | Highlander | 2021 | POWER TRAIN | 229 | 11439378 | 11474288 |
| Toyota | Highlander | 2021 | SERVICE BRAKES | 67 | 11406776 | 11419420 |
| Toyota | Highlander | 2021 | VISIBILITY/WIPER | 10 | 11416722 | 11428182 |
| Toyota | Highlander | 2022 | AIR BAGS | 32 | 11473299 | 11478125 |
| Toyota | Highlander | 2022 | ELECTRICAL SYSTEM | 23 | 11470228 | 11488669 |
| Toyota | Highlander | 2022 | ENGINE | 11 | 11473299 | 11478125 |
| Toyota | Highlander | 2022 | EXTERIOR LIGHTING | 12 | 11495929 | 11572775 |
| Toyota | Highlander | 2022 | FORWARD COLLISION AVOIDANCE | 22 | 11493170 | 11499811 |
| Toyota | Highlander | 2022 | FUEL/PROPULSION SYSTEM | 10 | 11451756 | 11453159 |
| Toyota | Highlander | 2022 | LANE DEPARTURE | 11 | 11472443 | 11499719 |
| Toyota | Highlander | 2022 | POWER TRAIN | 55 | 11486230 | 11486821 |
| Toyota | Highlander | 2022 | SERVICE BRAKES | 38 | 11460425 | 11468032 |
| Toyota | Highlander | 2022 | VISIBILITY/WIPER | 10 | 11470049 | 11479705 |
| Toyota | Highlander | 2023 | AIR BAGS | 12 | 11563885 | 11563886 |
| Toyota | Highlander | 2023 | ENGINE | 28 | 11531857 | 11534090 |
| Toyota | Highlander | 2023 | FUEL/PROPULSION SYSTEM | 16 | 11534843 | 11535351 |
| Toyota | Highlander | 2023 | POWER TRAIN | 20 | 11534090 | 11535351 |
| Toyota | Highlander | 2023 | SERVICE BRAKES | 20 | 11507296 | 11546245 |
| Toyota | RAV4 | 2021 | ELECTRICAL SYSTEM | 47 | 11399292 | 11403428 |
| Toyota | RAV4 | 2021 | ENGINE | 41 | 11416598 | 11478860 |
| Toyota | RAV4 | 2021 | FORWARD COLLISION AVOIDANCE | 18 | 11428721 | 11461952 |
| Toyota | RAV4 | 2021 | FUEL/PROPULSION SYSTEM | 21 | 11353782 | 11387955 |
| Toyota | RAV4 | 2021 | LANE DEPARTURE | 10 | 11398108 | 11399292 |
| Toyota | RAV4 | 2021 | POWER TRAIN | 23 | 11382724 | 11403677 |
| Toyota | RAV4 | 2021 | SEATS | 18 | 11442674 | 11614611 |
| Toyota | RAV4 | 2021 | SERVICE BRAKES | 21 | 11415942 | 11428721 |
| Toyota | RAV4 | 2021 | STEERING | 21 | 11398108 | 11414647 |
| Toyota | RAV4 | 2021 | STRUCTURE | 21 | 11403428 | 11448976 |
| Toyota | RAV4 | 2021 | VISIBILITY | 12 | 11364557 | 11534866 |
| Toyota | RAV4 | 2021 | VISIBILITY/WIPER | 19 | 11386212 | 11419505 |
| Toyota | RAV4 | 2022 | ELECTRICAL SYSTEM | 41 | 11457339 | 11492580 |
| Toyota | RAV4 | 2022 | ENGINE | 28 | 11457339 | 11491162 |
| Toyota | RAV4 | 2022 | FORWARD COLLISION AVOIDANCE | 11 | 11470826 | 11472948 |
| Toyota | RAV4 | 2022 | FUEL/PROPULSION SYSTEM | 10 | 11457225 | 11457339 |
| Toyota | RAV4 | 2022 | POWER TRAIN | 11 | 11477951 | 11491162 |
| Toyota | RAV4 | 2022 | STEERING | 20 | 11489690 | 11536716 |
| Toyota | RAV4 | 2022 | STRUCTURE | 19 | 11527249 | 11577399 |
| Toyota | RAV4 | 2023 | ENGINE | 25 | 11499456 | 11541150 |
| Toyota | RAV4 | 2023 | FORWARD COLLISION AVOIDANCE | 18 | 11518271 | 11566778 |
| Toyota | RAV4 | 2023 | FUEL/PROPULSION SYSTEM | 11 | 11538017 | 11549454 |
| Toyota | RAV4 | 2023 | POWER TRAIN | 11 | 11515720 | 11561314 |
| Toyota | RAV4 | 2023 | SERVICE BRAKES | 18 | 11541150 | 11552337 |
| Toyota | RAV4 | 2023 | STEERING | 27 | 11499456 | 11569688 |
| Toyota | RAV4 | 2023 | STRUCTURE | 10 | 11575108 | 11583710 |
| Toyota | RAV4 | 2023 | VISIBILITY/WIPER | 11 | 11535223 | 11544876 |
| Toyota | Tacoma | 2021 | ENGINE | 12 | 11398320 | 11427804 |
| Toyota | Tacoma | 2021 | POWER TRAIN | 14 | 11408651 | 11412879 |
| Toyota | Tacoma | 2021 | SERVICE BRAKES | 12 | 11397696 | 11430224 |
| Toyota | Tacoma | 2023 | ELECTRICAL SYSTEM | 12 | 11558608 | 11566373 |

Total uncovered components (PULL 1): 387.

## 4. Ranking (PULL 1 data)

Ranked by total complaints in uncovered components across the three model years; ties by make then model alphabetically.

| Rank | Make | Model | Uncovered complaints (3 years) |
|---|---|---|---|
| 1 | Chevrolet | Silverado 1500 | 1722 |
| 2 | GMC | Sierra 1500 | 1518 |
| 3 | Nissan | Rogue | 1315 |
| 4 | Jeep | Grand Cherokee | 931 |
| 5 | Honda | CR-V | 857 |
| 6 | Chevrolet | Tahoe | 782 |
| 7 | Ram | 1500 | 781 |
| 8 | Toyota | Highlander | 744 |
| 9 | Jeep | Wrangler | 722 |
| 10 | Subaru | Outback | 692 |
| 11 | Honda | Pilot | 666 |
| 12 | Ford | Bronco Sport | 658 |
| 13 | Hyundai | Tucson | 589 |
| 14 | Toyota | RAV4 | 543 |
| 15 | Honda | Accord | 514 |
| 16 | Honda | Civic | 471 |
| 17 | Chevrolet | Equinox | 302 |
| 18 | Subaru | Forester | 299 |
| 19 | Toyota | Corolla | 210 |
| 20 | Chevrolet | Traverse | 176 |
| 21 | Kia | Sportage | 171 |
| 22 | Ford | Escape | 151 |
| 23 | Ford | Edge | 103 |
| 24 | Toyota | Tacoma | 50 |
| 25 | Toyota | Camry | 35 |

## Changes (PULL 1 → PULL 2)

PULL 2 has not run yet. This report will be updated after PULL 2 with the changes table (new / gone / changed counts and both row counts).

## Proof — PULL 1

Source time (earliest Date header of PULL 1): Wed, 04 Nov 2026 12:20:07 GMT

| Request | UTC time | Count | Date header |
|---|---|---|---|
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Chevrolet/modelyear/2021?format=json` | 2026-11-04T12:20:07Z | 29 | Wed, 04 Nov 2026 12:20:07 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Chevrolet/modelyear/2022?format=json` | 2026-11-04T12:20:09Z | 35 | Wed, 04 Nov 2026 12:20:10 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Chevrolet/modelyear/2023?format=json` | 2026-11-04T12:20:12Z | 32 | Wed, 04 Nov 2026 12:20:12 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ford/modelyear/2021?format=json` | 2026-11-04T12:20:14Z | 51 | Wed, 04 Nov 2026 12:20:15 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ford/modelyear/2022?format=json` | 2026-11-04T12:20:17Z | 51 | Wed, 04 Nov 2026 12:20:18 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ford/modelyear/2023?format=json` | 2026-11-04T12:20:20Z | 50 | Wed, 04 Nov 2026 12:20:21 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/GMC/modelyear/2021?format=json` | 2026-11-04T12:20:22Z | 7 | Wed, 04 Nov 2026 12:20:22 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/GMC/modelyear/2022?format=json` | 2026-11-04T12:20:23Z | 10 | Wed, 04 Nov 2026 12:20:24 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/GMC/modelyear/2023?format=json` | 2026-11-04T12:20:24Z | 9 | Wed, 04 Nov 2026 12:20:25 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Honda/modelyear/2021?format=json` | 2026-11-04T12:20:26Z | 82 | Wed, 04 Nov 2026 12:20:27 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Honda/modelyear/2022?format=json` | 2026-11-04T12:20:27Z | 81 | Wed, 04 Nov 2026 12:20:28 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Honda/modelyear/2023?format=json` | 2026-11-04T12:20:29Z | 83 | Wed, 04 Nov 2026 12:20:30 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Hyundai/modelyear/2021?format=json` | 2026-11-04T12:20:30Z | 14 | Wed, 04 Nov 2026 12:20:31 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Hyundai/modelyear/2022?format=json` | 2026-11-04T12:20:32Z | 17 | Wed, 04 Nov 2026 12:20:32 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Hyundai/modelyear/2023?format=json` | 2026-11-04T12:20:36Z | 16 | Wed, 04 Nov 2026 12:20:37 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Jeep/modelyear/2021?format=json` | 2026-11-04T12:20:37Z | 9 | Wed, 04 Nov 2026 12:20:38 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Jeep/modelyear/2022?format=json` | 2026-11-04T12:20:39Z | 11 | Wed, 04 Nov 2026 12:20:40 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Jeep/modelyear/2023?format=json` | 2026-11-04T12:20:41Z | 11 | Wed, 04 Nov 2026 12:20:42 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Kia/modelyear/2021?format=json` | 2026-11-04T12:20:45Z | 12 | Wed, 04 Nov 2026 12:20:46 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Kia/modelyear/2022?format=json` | 2026-11-04T12:20:48Z | 13 | Wed, 04 Nov 2026 12:20:49 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Kia/modelyear/2023?format=json` | 2026-11-04T12:20:50Z | 14 | Wed, 04 Nov 2026 12:20:51 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Nissan/modelyear/2021?format=json` | 2026-11-04T12:20:53Z | 28 | Wed, 04 Nov 2026 12:20:53 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Nissan/modelyear/2022?format=json` | 2026-11-04T12:20:56Z | 25 | Wed, 04 Nov 2026 12:20:57 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Nissan/modelyear/2023?format=json` | 2026-11-04T12:20:58Z | 16 | Wed, 04 Nov 2026 12:20:59 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ram/modelyear/2021?format=json` | 2026-11-04T12:21:01Z | 111 | Wed, 04 Nov 2026 12:21:01 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ram/modelyear/2022?format=json` | 2026-11-04T12:21:03Z | 113 | Wed, 04 Nov 2026 12:21:04 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ram/modelyear/2023?format=json` | 2026-11-04T12:21:05Z | 113 | Wed, 04 Nov 2026 12:21:06 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Subaru/modelyear/2021?format=json` | 2026-11-04T12:21:07Z | 8 | Wed, 04 Nov 2026 12:21:08 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Subaru/modelyear/2022?format=json` | 2026-11-04T12:21:08Z | 8 | Wed, 04 Nov 2026 12:21:09 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Subaru/modelyear/2023?format=json` | 2026-11-04T12:21:10Z | 9 | Wed, 04 Nov 2026 12:21:10 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Toyota/modelyear/2021?format=json` | 2026-11-04T12:21:11Z | 18 | Wed, 04 Nov 2026 12:21:12 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Toyota/modelyear/2022?format=json` | 2026-11-04T12:21:13Z | 19 | Wed, 04 Nov 2026 12:21:14 GMT |
| `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Toyota/modelyear/2023?format=json` | 2026-11-04T12:21:14Z | 20 | Wed, 04 Nov 2026 12:21:15 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2021` | 2026-11-04T12:21:20Z | 855 | Wed, 04 Nov 2026 12:21:20 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2021` | 2026-11-04T12:21:29Z | 8 | Wed, 04 Nov 2026 12:21:29 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2021` | 2026-11-04T12:21:34Z | 855 | Wed, 04 Nov 2026 12:21:34 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2022` | 2026-11-04T12:21:37Z | 6 | Wed, 04 Nov 2026 12:21:37 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2022` | 2026-11-04T12:21:42Z | 656 | Wed, 04 Nov 2026 12:21:42 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2023` | 2026-11-04T12:21:44Z | 3 | Wed, 04 Nov 2026 12:21:45 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2023` | 2026-11-04T12:21:48Z | 391 | Wed, 04 Nov 2026 12:21:48 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ram&model=1500&modelYear=2021` | 2026-11-04T12:21:53Z | 686 | Wed, 04 Nov 2026 12:21:53 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ram&model=1500&modelYear=2021` | 2026-11-04T12:21:55Z | 15 | Wed, 04 Nov 2026 12:21:56 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ram&model=1500&modelYear=2021` | 2026-11-04T12:21:58Z | 686 | Wed, 04 Nov 2026 12:21:58 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ram&model=1500&modelYear=2022` | 2026-11-04T12:22:02Z | 16 | Wed, 04 Nov 2026 12:22:02 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ram&model=1500&modelYear=2022` | 2026-11-04T12:22:07Z | 0 | Wed, 04 Nov 2026 12:22:08 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ram&model=1500&modelYear=2023` | 2026-11-04T12:22:10Z | 11 | Wed, 04 Nov 2026 12:22:11 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ram&model=1500&modelYear=2023` | 2026-11-04T12:22:17Z | 0 | Wed, 04 Nov 2026 12:22:17 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra%201500&modelYear=2021` | 2026-11-04T12:22:23Z | 601 | Wed, 04 Nov 2026 12:22:22 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=GMC&model=Sierra%201500&modelYear=2021` | 2026-11-04T12:22:33Z | 7 | Wed, 04 Nov 2026 12:22:34 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra%201500&modelYear=2021` | 2026-11-04T12:22:38Z | 601 | Wed, 04 Nov 2026 12:22:37 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=GMC&model=Sierra%201500&modelYear=2022` | 2026-11-04T12:22:40Z | 6 | Wed, 04 Nov 2026 12:22:41 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra%201500&modelYear=2022` | 2026-11-04T12:22:46Z | 603 | Wed, 04 Nov 2026 12:22:45 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=GMC&model=Sierra%201500&modelYear=2023` | 2026-11-04T12:22:50Z | 3 | Wed, 04 Nov 2026 12:22:50 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra%201500&modelYear=2023` | 2026-11-04T12:22:55Z | 507 | Wed, 04 Nov 2026 12:22:54 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=RAV4&modelYear=2021` | 2026-11-04T12:23:00Z | 389 | Wed, 04 Nov 2026 12:23:00 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=RAV4&modelYear=2021` | 2026-11-04T12:23:04Z | 1 | Wed, 04 Nov 2026 12:23:04 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=RAV4&modelYear=2021` | 2026-11-04T12:23:11Z | 389 | Wed, 04 Nov 2026 12:23:08 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=RAV4&modelYear=2022` | 2026-11-04T12:23:12Z | 1 | Wed, 04 Nov 2026 12:23:13 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=RAV4&modelYear=2022` | 2026-11-04T12:23:14Z | 150 | Wed, 04 Nov 2026 12:23:15 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=RAV4&modelYear=2023` | 2026-11-04T12:23:16Z | 3 | Wed, 04 Nov 2026 12:23:17 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=RAV4&modelYear=2023` | 2026-11-04T12:23:18Z | 164 | Wed, 04 Nov 2026 12:23:19 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=CR-V&modelYear=2021` | 2026-11-04T12:23:21Z | 341 | Wed, 04 Nov 2026 12:23:22 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=CR-V&modelYear=2021` | 2026-11-04T12:23:22Z | 4 | Wed, 04 Nov 2026 12:23:23 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=CR-V&modelYear=2021` | 2026-11-04T12:23:25Z | 341 | Wed, 04 Nov 2026 12:23:25 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=CR-V&modelYear=2022` | 2026-11-04T12:23:26Z | 3 | Wed, 04 Nov 2026 12:23:27 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=CR-V&modelYear=2022` | 2026-11-04T12:23:29Z | 269 | Wed, 04 Nov 2026 12:23:29 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=CR-V&modelYear=2023` | 2026-11-04T12:23:31Z | 3 | Wed, 04 Nov 2026 12:23:31 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=CR-V&modelYear=2023` | 2026-11-04T12:23:37Z | 517 | Wed, 04 Nov 2026 12:23:37 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Camry&modelYear=2021` | 2026-11-04T12:23:42Z | 158 | Wed, 04 Nov 2026 12:23:42 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Camry&modelYear=2021` | 2026-11-04T12:23:46Z | 1 | Wed, 04 Nov 2026 12:23:46 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Camry&modelYear=2021` | 2026-11-04T12:23:49Z | 158 | Wed, 04 Nov 2026 12:23:49 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Camry&modelYear=2022` | 2026-11-04T12:23:52Z | 1 | Wed, 04 Nov 2026 12:23:52 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Camry&modelYear=2022` | 2026-11-04T12:23:55Z | 65 | Wed, 04 Nov 2026 12:23:55 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Camry&modelYear=2023` | 2026-11-04T12:23:57Z | 2 | Wed, 04 Nov 2026 12:23:58 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Camry&modelYear=2023` | 2026-11-04T12:24:01Z | 65 | Wed, 04 Nov 2026 12:24:01 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Nissan&model=Rogue&modelYear=2021` | 2026-11-04T12:24:05Z | 295 | Wed, 04 Nov 2026 12:24:05 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Nissan&model=Rogue&modelYear=2021` | 2026-11-04T12:24:08Z | 10 | Wed, 04 Nov 2026 12:24:09 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Nissan&model=Rogue&modelYear=2021` | 2026-11-04T12:24:12Z | 295 | Wed, 04 Nov 2026 12:24:11 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Nissan&model=Rogue&modelYear=2022` | 2026-11-04T12:24:15Z | 6 | Wed, 04 Nov 2026 12:24:15 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Nissan&model=Rogue&modelYear=2022` | 2026-11-04T12:24:18Z | 270 | Wed, 04 Nov 2026 12:24:18 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Nissan&model=Rogue&modelYear=2023` | 2026-11-04T12:24:19Z | 6 | Wed, 04 Nov 2026 12:24:20 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Nissan&model=Rogue&modelYear=2023` | 2026-11-04T12:24:24Z | 766 | Wed, 04 Nov 2026 12:24:25 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Equinox&modelYear=2021` | 2026-11-04T12:24:27Z | 100 | Wed, 04 Nov 2026 12:24:27 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Equinox&modelYear=2021` | 2026-11-04T12:24:28Z | 4 | Wed, 04 Nov 2026 12:24:29 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Equinox&modelYear=2021` | 2026-11-04T12:24:30Z | 100 | Wed, 04 Nov 2026 12:24:30 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Equinox&modelYear=2022` | 2026-11-04T12:24:31Z | 5 | Wed, 04 Nov 2026 12:24:32 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Equinox&modelYear=2022` | 2026-11-04T12:24:34Z | 183 | Wed, 04 Nov 2026 12:24:35 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Equinox&modelYear=2023` | 2026-11-04T12:24:37Z | 3 | Wed, 04 Nov 2026 12:24:37 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Equinox&modelYear=2023` | 2026-11-04T12:24:42Z | 99 | Wed, 04 Nov 2026 12:24:42 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Tacoma&modelYear=2021` | 2026-11-04T12:24:44Z | 81 | Wed, 04 Nov 2026 12:24:44 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Tacoma&modelYear=2021` | 2026-11-04T12:24:48Z | 0 | Wed, 04 Nov 2026 12:24:49 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Tacoma&modelYear=2021` | 2026-11-04T12:24:51Z | 81 | Wed, 04 Nov 2026 12:24:52 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Tacoma&modelYear=2022` | 2026-11-04T12:24:54Z | 3 | Wed, 04 Nov 2026 12:24:54 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Tacoma&modelYear=2022` | 2026-11-04T12:24:56Z | 59 | Wed, 04 Nov 2026 12:24:56 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Tacoma&modelYear=2023` | 2026-11-04T12:29:20Z | 4 | Wed, 04 Nov 2026 12:29:22 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Tacoma&modelYear=2023` | 2026-11-04T12:29:22Z | 54 | Wed, 04 Nov 2026 12:29:25 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Civic&modelYear=2021` | 2026-11-04T12:30:01Z | 148 | Wed, 04 Nov 2026 12:30:05 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Civic&modelYear=2021` | 2026-11-04T12:30:04Z | 4 | Wed, 04 Nov 2026 12:30:08 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Civic&modelYear=2021` | 2026-11-04T12:30:07Z | 148 | Wed, 04 Nov 2026 12:30:11 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Civic&modelYear=2022` | 2026-11-04T12:30:10Z | 4 | Wed, 04 Nov 2026 12:30:13 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Civic&modelYear=2022` | 2026-11-04T12:30:13Z | 886 | Wed, 04 Nov 2026 12:30:17 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Civic&modelYear=2023` | 2026-11-04T12:30:17Z | 4 | Wed, 04 Nov 2026 12:30:20 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Civic&modelYear=2023` | 2026-11-04T12:30:19Z | 0 | Wed, 04 Nov 2026 12:30:23 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Accord&modelYear=2021` | 2026-11-04T12:30:22Z | 246 | Wed, 04 Nov 2026 12:30:27 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Accord&modelYear=2021` | 2026-11-04T12:30:26Z | 4 | Wed, 04 Nov 2026 12:30:30 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Accord&modelYear=2021` | 2026-11-04T12:30:30Z | 246 | Wed, 04 Nov 2026 12:30:34 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Accord&modelYear=2022` | 2026-11-04T12:30:34Z | 4 | Wed, 04 Nov 2026 12:30:39 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Accord&modelYear=2022` | 2026-11-04T12:30:38Z | 262 | Wed, 04 Nov 2026 12:30:43 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Escape&modelYear=2021` | 2026-11-04T12:34:43Z | 355 | Wed, 04 Nov 2026 12:35:28 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Escape&modelYear=2021` | 2026-11-04T12:35:28Z | 19 | Wed, 04 Nov 2026 12:35:31 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Escape&modelYear=2021` | 2026-11-04T12:35:31Z | 355 | Wed, 04 Nov 2026 12:35:36 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Escape&modelYear=2022` | 2026-11-04T12:35:35Z | 19 | Wed, 04 Nov 2026 12:35:43 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Escape&modelYear=2022` | 2026-11-04T12:35:43Z | 238 | Wed, 04 Nov 2026 12:35:47 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Escape&modelYear=2023` | 2026-11-04T12:35:47Z | 11 | Wed, 04 Nov 2026 12:35:52 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Escape&modelYear=2023` | 2026-11-04T12:35:52Z | 102 | Wed, 04 Nov 2026 12:35:57 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Corolla&modelYear=2021` | 2026-11-04T12:35:56Z | 188 | Wed, 04 Nov 2026 12:36:01 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Corolla&modelYear=2021` | 2026-11-04T12:36:00Z | 1 | Wed, 04 Nov 2026 12:36:03 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Corolla&modelYear=2021` | 2026-11-04T12:36:02Z | 188 | Wed, 04 Nov 2026 12:36:06 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Corolla&modelYear=2022` | 2026-11-04T12:36:06Z | 0 | Wed, 04 Nov 2026 12:36:08 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Corolla&modelYear=2022` | 2026-11-04T12:36:07Z | 102 | Wed, 04 Nov 2026 12:36:11 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Corolla&modelYear=2023` | 2026-11-04T12:36:10Z | 3 | Wed, 04 Nov 2026 12:36:13 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Corolla&modelYear=2023` | 2026-11-04T12:36:13Z | 74 | Wed, 04 Nov 2026 12:36:16 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2021` | 2026-11-04T12:36:15Z | 411 | Wed, 04 Nov 2026 12:36:19 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2021` | 2026-11-04T12:36:19Z | 12 | Wed, 04 Nov 2026 12:36:21 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2021` | 2026-11-04T12:36:20Z | 411 | Wed, 04 Nov 2026 12:36:24 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2022` | 2026-11-04T12:36:24Z | 13 | Wed, 04 Nov 2026 12:36:27 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2022` | 2026-11-04T12:36:26Z | 379 | Wed, 04 Nov 2026 12:36:30 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2023` | 2026-11-04T12:36:30Z | 21 | Wed, 04 Nov 2026 12:36:34 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2023` | 2026-11-04T12:36:33Z | 408 | Wed, 04 Nov 2026 12:36:37 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Edge&modelYear=2021` | 2026-11-04T12:36:37Z | 114 | Wed, 04 Nov 2026 12:36:40 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Edge&modelYear=2021` | 2026-11-04T12:36:39Z | 7 | Wed, 04 Nov 2026 12:36:42 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Edge&modelYear=2021` | 2026-11-04T12:36:41Z | 114 | Wed, 04 Nov 2026 12:36:43 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Edge&modelYear=2022` | 2026-11-04T12:36:43Z | 5 | Wed, 04 Nov 2026 12:36:45 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Edge&modelYear=2022` | 2026-11-04T12:36:45Z | 135 | Wed, 04 Nov 2026 12:36:48 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Edge&modelYear=2023` | 2026-11-04T12:36:48Z | 4 | Wed, 04 Nov 2026 12:36:51 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Edge&modelYear=2023` | 2026-11-04T12:36:51Z | 23 | Wed, 04 Nov 2026 12:36:55 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Forester&modelYear=2021` | 2026-11-04T12:36:59Z | 215 | Wed, 04 Nov 2026 12:37:03 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Forester&modelYear=2021` | 2026-11-04T12:37:03Z | 0 | Wed, 04 Nov 2026 12:37:06 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Forester&modelYear=2021` | 2026-11-04T12:37:05Z | 215 | Wed, 04 Nov 2026 12:37:08 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Forester&modelYear=2022` | 2026-11-04T12:37:07Z | 1 | Wed, 04 Nov 2026 12:37:10 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Forester&modelYear=2022` | 2026-11-04T12:37:09Z | 100 | Wed, 04 Nov 2026 12:37:12 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Forester&modelYear=2023` | 2026-11-04T12:37:12Z | 1 | Wed, 04 Nov 2026 12:37:14 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Forester&modelYear=2023` | 2026-11-04T12:37:13Z | 74 | Wed, 04 Nov 2026 12:37:16 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Wrangler&modelYear=2021` | 2026-11-04T12:37:16Z | 960 | Wed, 04 Nov 2026 12:37:20 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Wrangler&modelYear=2021` | 2026-11-04T12:37:20Z | 15 | Wed, 04 Nov 2026 12:37:23 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Wrangler&modelYear=2021` | 2026-11-04T12:37:22Z | 960 | Wed, 04 Nov 2026 12:37:27 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Wrangler&modelYear=2022` | 2026-11-04T12:37:27Z | 15 | Wed, 04 Nov 2026 12:37:30 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Wrangler&modelYear=2022` | 2026-11-04T12:37:30Z | 413 | Wed, 04 Nov 2026 12:37:33 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Wrangler&modelYear=2023` | 2026-11-04T12:37:33Z | 14 | Wed, 04 Nov 2026 12:37:36 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Wrangler&modelYear=2023` | 2026-11-04T12:37:35Z | 376 | Wed, 04 Nov 2026 12:37:39 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Highlander&modelYear=2021` | 2026-11-04T12:37:39Z | 535 | Wed, 04 Nov 2026 12:37:43 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Highlander&modelYear=2021` | 2026-11-04T12:37:42Z | 4 | Wed, 04 Nov 2026 12:37:45 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Highlander&modelYear=2021` | 2026-11-04T12:37:44Z | 535 | Wed, 04 Nov 2026 12:37:47 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Highlander&modelYear=2022` | 2026-11-04T12:37:47Z | 5 | Wed, 04 Nov 2026 12:37:50 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Highlander&modelYear=2022` | 2026-11-04T12:37:49Z | 266 | Wed, 04 Nov 2026 12:37:52 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Highlander&modelYear=2023` | 2026-11-04T12:37:52Z | 9 | Wed, 04 Nov 2026 12:37:54 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Highlander&modelYear=2023` | 2026-11-04T12:37:53Z | 189 | Wed, 04 Nov 2026 12:37:56 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Hyundai&model=Tucson&modelYear=2021` | 2026-11-04T12:37:56Z | 80 | Wed, 04 Nov 2026 12:37:59 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Hyundai&model=Tucson&modelYear=2021` | 2026-11-04T12:37:59Z | 1 | Wed, 04 Nov 2026 12:38:01 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Hyundai&model=Tucson&modelYear=2021` | 2026-11-04T12:38:01Z | 80 | Wed, 04 Nov 2026 12:38:04 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Hyundai&model=Tucson&modelYear=2022` | 2026-11-04T12:38:03Z | 3 | Wed, 04 Nov 2026 12:38:06 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Hyundai&model=Tucson&modelYear=2022` | 2026-11-04T12:38:05Z | 390 | Wed, 04 Nov 2026 12:38:09 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Hyundai&model=Tucson&modelYear=2023` | 2026-11-04T12:38:09Z | 2 | Wed, 04 Nov 2026 12:38:11 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Hyundai&model=Tucson&modelYear=2023` | 2026-11-04T12:38:11Z | 136 | Wed, 04 Nov 2026 12:38:15 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2021` | 2026-11-04T12:38:15Z | 465 | Wed, 04 Nov 2026 12:38:18 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2021` | 2026-11-04T12:38:18Z | 16 | Wed, 04 Nov 2026 12:38:21 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2021` | 2026-11-04T12:38:20Z | 465 | Wed, 04 Nov 2026 12:38:24 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2022` | 2026-11-04T12:38:23Z | 4 | Wed, 04 Nov 2026 12:38:26 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2022` | 2026-11-04T12:38:25Z | 197 | Wed, 04 Nov 2026 12:38:29 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2023` | 2026-11-04T12:38:29Z | 5 | Wed, 04 Nov 2026 12:38:32 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2023` | 2026-11-04T12:38:31Z | 234 | Wed, 04 Nov 2026 12:38:35 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Pilot&modelYear=2021` | 2026-11-04T12:38:38Z | 454 | Wed, 04 Nov 2026 12:38:44 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Pilot&modelYear=2021` | 2026-11-04T12:38:44Z | 10 | Wed, 04 Nov 2026 12:38:47 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Pilot&modelYear=2021` | 2026-11-04T12:38:46Z | 454 | Wed, 04 Nov 2026 12:38:49 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Pilot&modelYear=2022` | 2026-11-04T12:38:49Z | 5 | Wed, 04 Nov 2026 12:38:52 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Pilot&modelYear=2022` | 2026-11-04T12:38:52Z | 174 | Wed, 04 Nov 2026 12:38:55 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Pilot&modelYear=2023` | 2026-11-04T12:38:54Z | 5 | Wed, 04 Nov 2026 12:38:58 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Pilot&modelYear=2023` | 2026-11-04T12:38:57Z | 149 | Wed, 04 Nov 2026 12:39:01 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Kia&model=Sportage&modelYear=2021` | 2026-11-04T12:39:00Z | 54 | Wed, 04 Nov 2026 12:39:04 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Kia&model=Sportage&modelYear=2021` | 2026-11-04T12:39:03Z | 2 | Wed, 04 Nov 2026 12:39:07 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Kia&model=Sportage&modelYear=2021` | 2026-11-04T12:39:07Z | 54 | Wed, 04 Nov 2026 12:39:09 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Kia&model=Sportage&modelYear=2022` | 2026-11-04T12:39:08Z | 1 | Wed, 04 Nov 2026 12:39:11 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Kia&model=Sportage&modelYear=2022` | 2026-11-04T12:39:11Z | 47 | Wed, 04 Nov 2026 12:39:13 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Kia&model=Sportage&modelYear=2023` | 2026-11-04T12:39:13Z | 6 | Wed, 04 Nov 2026 12:39:15 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Kia&model=Sportage&modelYear=2023` | 2026-11-04T12:39:15Z | 196 | Wed, 04 Nov 2026 12:39:18 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Outback&modelYear=2021` | 2026-11-04T12:39:18Z | 299 | Wed, 04 Nov 2026 12:39:21 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Outback&modelYear=2021` | 2026-11-04T12:39:21Z | 4 | Wed, 04 Nov 2026 12:39:24 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Outback&modelYear=2021` | 2026-11-04T12:39:23Z | 299 | Wed, 04 Nov 2026 12:39:26 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Outback&modelYear=2022` | 2026-11-04T12:39:26Z | 4 | Wed, 04 Nov 2026 12:39:28 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Outback&modelYear=2022` | 2026-11-04T12:39:28Z | 465 | Wed, 04 Nov 2026 12:39:32 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Outback&modelYear=2023` | 2026-11-04T12:39:32Z | 2 | Wed, 04 Nov 2026 12:39:36 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Outback&modelYear=2023` | 2026-11-04T12:39:35Z | 89 | Wed, 04 Nov 2026 12:39:38 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Traverse&modelYear=2021` | 2026-11-04T12:39:38Z | 94 | Wed, 04 Nov 2026 12:39:41 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Traverse&modelYear=2021` | 2026-11-04T12:39:41Z | 3 | Wed, 04 Nov 2026 12:39:44 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Traverse&modelYear=2021` | 2026-11-04T12:39:44Z | 94 | Wed, 04 Nov 2026 12:39:47 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Traverse&modelYear=2022` | 2026-11-04T12:39:47Z | 1 | Wed, 04 Nov 2026 12:39:50 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Traverse&modelYear=2022` | 2026-11-04T12:39:49Z | 103 | Wed, 04 Nov 2026 12:39:52 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Traverse&modelYear=2023` | 2026-11-04T12:39:52Z | 2 | Wed, 04 Nov 2026 12:39:54 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Traverse&modelYear=2023` | 2026-11-04T12:39:54Z | 95 | Wed, 04 Nov 2026 12:39:57 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2021` | 2026-11-04T12:39:56Z | 713 | Wed, 04 Nov 2026 12:40:00 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2021` | 2026-11-04T12:40:00Z | 16 | Wed, 04 Nov 2026 12:40:02 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2021` | 2026-11-04T12:40:02Z | 713 | Wed, 04 Nov 2026 12:40:06 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2022` | 2026-11-04T12:40:06Z | 15 | Wed, 04 Nov 2026 12:40:10 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2022` | 2026-11-04T12:40:09Z | 370 | Wed, 04 Nov 2026 12:40:13 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2023` | 2026-11-04T12:40:13Z | 14 | Wed, 04 Nov 2026 12:40:16 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2023` | 2026-11-04T12:40:16Z | 163 | Wed, 04 Nov 2026 12:40:19 GMT |
| `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Accord&modelYear=2023` | 2026-11-04T12:41:45Z | 5 | Wed, 04 Nov 2026 12:41:48 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Accord&modelYear=2023` | 2026-11-04T12:41:47Z | 0 | Wed, 04 Nov 2026 12:41:52 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado&modelYear=2021` | 2026-11-04T12:43:28Z | 0 | Wed, 04 Nov 2026 12:43:31 GMT |
| `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra&modelYear=2021` | 2026-11-04T12:43:30Z | 0 | Wed, 04 Nov 2026 12:43:33 GMT |

### Verbatim raw excerpts — PULL 1

Each excerpt below is the verbatim first 1,000 bytes of the saved raw response body for that request, unmodified (no re-serialization, no pretty-printing), with its HTTP Date header and UTC retrieval time.

### vpic_Chevrolet_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Chevrolet/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:20:07Z | HTTP Date: Wed, 04 Nov 2026 12:20:07 GMT | Count: 29 | bytes: 2423
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":29,"Message":"Results returned successfully","SearchCriteria":"Make:Chevrolet | ModelYear:2021","Results":[{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1829,"Model_Name":"Camaro"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1831,"Model_Name":"Corvette"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1834,"Model_Name":"Malibu"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1836,"Model_Name":"Spark"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1847,"Model_Name":"Equinox"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1850,"Model_Name":"Silverado"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1850,"Model_Name":"Silverado"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1851,"Model_Name":"Suburban"},{"Make_ID":46
```
### vpic_Chevrolet_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Chevrolet/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:20:09Z | HTTP Date: Wed, 04 Nov 2026 12:20:10 GMT | Count: 35 | bytes: 2917
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":35,"Message":"Results returned successfully","SearchCriteria":"Make:Chevrolet | ModelYear:2022","Results":[{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1829,"Model_Name":"Camaro"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1831,"Model_Name":"Corvette"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1834,"Model_Name":"Malibu"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1836,"Model_Name":"Spark"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1847,"Model_Name":"Equinox"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1850,"Model_Name":"Silverado"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1850,"Model_Name":"Silverado"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1851,"Model_Name":"Suburban"},{"Make_ID":46
```
### vpic_Chevrolet_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Chevrolet/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:20:12Z | HTTP Date: Wed, 04 Nov 2026 12:20:12 GMT | Count: 32 | bytes: 2668
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":32,"Message":"Results returned successfully","SearchCriteria":"Make:Chevrolet | ModelYear:2023","Results":[{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1829,"Model_Name":"Camaro"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1831,"Model_Name":"Corvette"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1834,"Model_Name":"Malibu"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1847,"Model_Name":"Equinox"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1848,"Model_Name":"Express"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1850,"Model_Name":"Silverado"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1850,"Model_Name":"Silverado"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1851,"Model_Name":"Suburban"},{"Make_ID":467,"Make_Name":"CHEVROLET","Model_ID":1852,"Model_Name":"Tahoe"},{"Make_ID":46
```
### vpic_Ford_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ford/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:20:14Z | HTTP Date: Wed, 04 Nov 2026 12:20:15 GMT | Count: 51 | bytes: 4269
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":51,"Message":"Results returned successfully","SearchCriteria":"Make:Ford | ModelYear:2021","Results":[{"Make_ID":1237,"Make_Name":"AFFORDABLE ALUMINUM","Model_ID":4563,"Model_Name":"Affordable Aluminum"},{"Make_ID":10240,"Make_Name":"AFFORDABLE TRAILERS","Model_ID":26910,"Model_Name":"Affordable Trailers"},{"Make_ID":5697,"Make_Name":"ASHFORD MFG","Model_ID":14916,"Model_Name":"Travel Park"},{"Make_ID":8578,"Make_Name":"BRADFORD #1","Model_ID":22551,"Model_Name":"Bradford #1"},{"Make_ID":6674,"Make_Name":"BRADFORD BUILT","Model_ID":18064,"Model_Name":"Bradford Built"},{"Make_ID":6579,"Make_Name":"CRANFORD RADIATOR INC.","Model_ID":17910,"Model_Name":"CRANFORD RADIATOR INC."},{"Make_ID":1298,"Make_Name":"EAGLE FORD TANKS & TRAILERS LLC","Model_ID":4645,"Model_Name":"Eagle Ford Tanks & Trailers LLC"},{"Make_ID":460,"Make_Name":"FORD","Model_ID":1781,"Model_Name":"Mustang"},{"Make_ID":460,"Make_Name":"FORD","Model_ID":1797,"Model_Name":"Edge"},{"Make_ID":460,"Make_Name":"FORD","M
```
### vpic_Ford_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ford/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:20:17Z | HTTP Date: Wed, 04 Nov 2026 12:20:18 GMT | Count: 51 | bytes: 4272
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":51,"Message":"Results returned successfully","SearchCriteria":"Make:Ford | ModelYear:2022","Results":[{"Make_ID":1237,"Make_Name":"AFFORDABLE ALUMINUM","Model_ID":4563,"Model_Name":"Affordable Aluminum"},{"Make_ID":10240,"Make_Name":"AFFORDABLE TRAILERS","Model_ID":26910,"Model_Name":"Affordable Trailers"},{"Make_ID":5697,"Make_Name":"ASHFORD MFG","Model_ID":14916,"Model_Name":"Travel Park"},{"Make_ID":8578,"Make_Name":"BRADFORD #1","Model_ID":22551,"Model_Name":"Bradford #1"},{"Make_ID":6674,"Make_Name":"BRADFORD BUILT","Model_ID":18064,"Model_Name":"Bradford Built"},{"Make_ID":6579,"Make_Name":"CRANFORD RADIATOR INC.","Model_ID":17910,"Model_Name":"CRANFORD RADIATOR INC."},{"Make_ID":1298,"Make_Name":"EAGLE FORD TANKS & TRAILERS LLC","Model_ID":4645,"Model_Name":"Eagle Ford Tanks & Trailers LLC"},{"Make_ID":460,"Make_Name":"FORD","Model_ID":1781,"Model_Name":"Mustang"},{"Make_ID":460,"Make_Name":"FORD","Model_ID":1797,"Model_Name":"Edge"},{"Make_ID":460,"Make_Name":"FORD","M
```
### vpic_Ford_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ford/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:20:20Z | HTTP Date: Wed, 04 Nov 2026 12:20:21 GMT | Count: 50 | bytes: 4202
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":50,"Message":"Results returned successfully","SearchCriteria":"Make:Ford | ModelYear:2023","Results":[{"Make_ID":1237,"Make_Name":"AFFORDABLE ALUMINUM","Model_ID":4563,"Model_Name":"Affordable Aluminum"},{"Make_ID":10240,"Make_Name":"AFFORDABLE TRAILERS","Model_ID":26910,"Model_Name":"Affordable Trailers"},{"Make_ID":5697,"Make_Name":"ASHFORD MFG","Model_ID":14916,"Model_Name":"Travel Park"},{"Make_ID":8578,"Make_Name":"BRADFORD #1","Model_ID":22551,"Model_Name":"Bradford #1"},{"Make_ID":6674,"Make_Name":"BRADFORD BUILT","Model_ID":18064,"Model_Name":"Bradford Built"},{"Make_ID":6579,"Make_Name":"CRANFORD RADIATOR INC.","Model_ID":17910,"Model_Name":"CRANFORD RADIATOR INC."},{"Make_ID":1298,"Make_Name":"EAGLE FORD TANKS & TRAILERS LLC","Model_ID":4645,"Model_Name":"Eagle Ford Tanks & Trailers LLC"},{"Make_ID":460,"Make_Name":"FORD","Model_ID":1781,"Model_Name":"Mustang"},{"Make_ID":460,"Make_Name":"FORD","Model_ID":1797,"Model_Name":"Edge"},{"Make_ID":460,"Make_Name":"FORD","M
```
### vpic_GMC_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/GMC/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:20:22Z | HTTP Date: Wed, 04 Nov 2026 12:20:22 GMT | Count: 7 | bytes: 616
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":7,"Message":"Results returned successfully","SearchCriteria":"Make:GMC | ModelYear:2021","Results":[{"Make_ID":472,"Make_Name":"GMC","Model_ID":1855,"Model_Name":"Acadia"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1856,"Model_Name":"Savana"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1857,"Model_Name":"Sierra"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1858,"Model_Name":"Terrain"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1859,"Model_Name":"Yukon"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":4093,"Model_Name":"Canyon"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":4579,"Model_Name":"Yukon XL"}]}
```
### vpic_GMC_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/GMC/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:20:23Z | HTTP Date: Wed, 04 Nov 2026 12:20:24 GMT | Count: 10 | bytes: 857
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":10,"Message":"Results returned successfully","SearchCriteria":"Make:GMC | ModelYear:2022","Results":[{"Make_ID":472,"Make_Name":"GMC","Model_ID":1855,"Model_Name":"Acadia"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1856,"Model_Name":"Savana"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1857,"Model_Name":"Sierra"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1858,"Model_Name":"Terrain"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1859,"Model_Name":"Yukon"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":4093,"Model_Name":"Canyon"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":4579,"Model_Name":"Yukon XL"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":24909,"Model_Name":"Sierra HD"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":24910,"Model_Name":"Sierra Limited"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":32046,"Model_Name":"Hummer EV Pickup"}]}
```
### vpic_GMC_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/GMC/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:20:24Z | HTTP Date: Wed, 04 Nov 2026 12:20:25 GMT | Count: 9 | bytes: 775
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":9,"Message":"Results returned successfully","SearchCriteria":"Make:GMC | ModelYear:2023","Results":[{"Make_ID":472,"Make_Name":"GMC","Model_ID":1855,"Model_Name":"Acadia"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1856,"Model_Name":"Savana"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1857,"Model_Name":"Sierra"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1858,"Model_Name":"Terrain"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":1859,"Model_Name":"Yukon"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":4093,"Model_Name":"Canyon"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":4579,"Model_Name":"Yukon XL"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":24909,"Model_Name":"Sierra HD"},{"Make_ID":472,"Make_Name":"GMC","Model_ID":32046,"Model_Name":"Hummer EV Pickup"}]}
```
### vpic_Honda_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Honda/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:20:26Z | HTTP Date: Wed, 04 Nov 2026 12:20:27 GMT | Count: 82 | bytes: 6556
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":82,"Message":"Results returned successfully","SearchCriteria":"Make:Honda | ModelYear:2021","Results":[{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1861,"Model_Name":"Accord"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1863,"Model_Name":"Civic"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1864,"Model_Name":"Pilot"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1865,"Model_Name":"CR-V"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1866,"Model_Name":"Ridgeline"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1869,"Model_Name":"Odyssey"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1870,"Model_Name":"Insight"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3249,"Model_Name":"Gold Wing"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3251,"Model_Name":"NC700X"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3252,"Model_Name":"Metropolitan"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3253,"Model_Name":"NPS50 (Ruckus)"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3264,"Mode
```
### vpic_Honda_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Honda/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:20:27Z | HTTP Date: Wed, 04 Nov 2026 12:20:28 GMT | Count: 81 | bytes: 6459
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":81,"Message":"Results returned successfully","SearchCriteria":"Make:Honda | ModelYear:2022","Results":[{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1861,"Model_Name":"Accord"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1863,"Model_Name":"Civic"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1864,"Model_Name":"Pilot"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1865,"Model_Name":"CR-V"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1866,"Model_Name":"Ridgeline"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1869,"Model_Name":"Odyssey"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1870,"Model_Name":"Insight"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3234,"Model_Name":"PCX150"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3249,"Model_Name":"Gold Wing"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3251,"Model_Name":"NC700X"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3252,"Model_Name":"Metropolitan"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3253,"Model_Name":
```
### vpic_Honda_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Honda/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:20:29Z | HTTP Date: Wed, 04 Nov 2026 12:20:30 GMT | Count: 83 | bytes: 6597
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":83,"Message":"Results returned successfully","SearchCriteria":"Make:Honda | ModelYear:2023","Results":[{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1861,"Model_Name":"Accord"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1863,"Model_Name":"Civic"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1864,"Model_Name":"Pilot"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1865,"Model_Name":"CR-V"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1866,"Model_Name":"Ridgeline"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":1869,"Model_Name":"Odyssey"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3234,"Model_Name":"PCX150"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3249,"Model_Name":"Gold Wing"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3251,"Model_Name":"NC700X"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3252,"Model_Name":"Metropolitan"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3253,"Model_Name":"NPS50 (Ruckus)"},{"Make_ID":474,"Make_Name":"HONDA","Model_ID":3255,"Model
```
### vpic_Hyundai_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Hyundai/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:20:30Z | HTTP Date: Wed, 04 Nov 2026 12:20:31 GMT | Count: 14 | bytes: 1280
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":14,"Message":"Results returned successfully","SearchCriteria":"Make:Hyundai | ModelYear:2021","Results":[{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2057,"Model_Name":"Santa Fe"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2058,"Model_Name":"Tucson"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2298,"Model_Name":"Veloster"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2459,"Model_Name":"Sonata"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2735,"Model_Name":"Elantra"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2773,"Model_Name":"Accent"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":21961,"Model_Name":"Ioniq"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":22249,"Model_Name":"Kona"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":25183,"Model_Name":"Nexo"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":25847,"Model_Name":"Palisade"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":26441,"Model_Name":"Venue"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_
```
### vpic_Hyundai_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Hyundai/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:20:32Z | HTTP Date: Wed, 04 Nov 2026 12:20:32 GMT | Count: 17 | bytes: 1518
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":17,"Message":"Results returned successfully","SearchCriteria":"Make:Hyundai | ModelYear:2022","Results":[{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2057,"Model_Name":"Santa Fe"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2058,"Model_Name":"Tucson"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2459,"Model_Name":"Sonata"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2735,"Model_Name":"Elantra"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2773,"Model_Name":"Accent"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":21961,"Model_Name":"Ioniq"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":22249,"Model_Name":"Kona"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":25183,"Model_Name":"Nexo"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":25847,"Model_Name":"Palisade"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":26441,"Model_Name":"Venue"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":28077,"Model_Name":"Veloster N"},{"Make_ID":498,"Make_Name":"HYUNDAI","Mod
```
### vpic_Hyundai_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Hyundai/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:20:36Z | HTTP Date: Wed, 04 Nov 2026 12:20:37 GMT | Count: 16 | bytes: 1440
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":16,"Message":"Results returned successfully","SearchCriteria":"Make:Hyundai | ModelYear:2023","Results":[{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2057,"Model_Name":"Santa Fe"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2058,"Model_Name":"Tucson"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2459,"Model_Name":"Sonata"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":2735,"Model_Name":"Elantra"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":22249,"Model_Name":"Kona"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":25183,"Model_Name":"Nexo"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":25847,"Model_Name":"Palisade"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":26441,"Model_Name":"Venue"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":28816,"Model_Name":"Santa Cruz"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":28983,"Model_Name":"Ioniq 5"},{"Make_ID":498,"Make_Name":"HYUNDAI","Model_ID":29258,"Model_Name":"Elantra N"},{"Make_ID":498,"Make_Name":"HYUNDAI
```
### vpic_Jeep_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Jeep/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:20:37Z | HTTP Date: Wed, 04 Nov 2026 12:20:38 GMT | Count: 9 | bytes: 802
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":9,"Message":"Results returned successfully","SearchCriteria":"Make:Jeep | ModelYear:2021","Results":[{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1943,"Model_Name":"Wrangler"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1946,"Model_Name":"Compass"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1949,"Model_Name":"Grand Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":6160,"Model_Name":"Renegade"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":25919,"Model_Name":"Gladiator"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":32375,"Model_Name":"Grand Cherokee L"}]}
```
### vpic_Jeep_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Jeep/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:20:39Z | HTTP Date: Wed, 04 Nov 2026 12:20:40 GMT | Count: 11 | bytes: 961
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":11,"Message":"Results returned successfully","SearchCriteria":"Make:Jeep | ModelYear:2022","Results":[{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1943,"Model_Name":"Wrangler"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1946,"Model_Name":"Compass"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1949,"Model_Name":"Grand Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":6160,"Model_Name":"Renegade"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":14871,"Model_Name":"Grand Wagoneer"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":14927,"Model_Name":"Wagoneer"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":25919,"Model_Name":"Gladiator"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":32375,"Model_Name":"Grand Cherokee L"}]}
```
### vpic_Jeep_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Jeep/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:20:41Z | HTTP Date: Wed, 04 Nov 2026 12:20:42 GMT | Count: 11 | bytes: 961
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":11,"Message":"Results returned successfully","SearchCriteria":"Make:Jeep | ModelYear:2023","Results":[{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1943,"Model_Name":"Wrangler"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1945,"Model_Name":"Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1946,"Model_Name":"Compass"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":1949,"Model_Name":"Grand Cherokee"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":6160,"Model_Name":"Renegade"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":14871,"Model_Name":"Grand Wagoneer"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":14927,"Model_Name":"Wagoneer"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":25919,"Model_Name":"Gladiator"},{"Make_ID":483,"Make_Name":"JEEP","Model_ID":32375,"Model_Name":"Grand Cherokee L"}]}
```
### vpic_Kia_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Kia/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:20:45Z | HTTP Date: Wed, 04 Nov 2026 12:20:46 GMT | Count: 12 | bytes: 1000
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":12,"Message":"Results returned successfully","SearchCriteria":"Make:Kia | ModelYear:2021","Results":[{"Make_ID":499,"Make_Name":"KIA","Model_ID":2299,"Model_Name":"Rio"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2460,"Model_Name":"Soul"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2462,"Model_Name":"Forte"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2740,"Model_Name":"Sedona"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2769,"Model_Name":"Sorento"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2770,"Model_Name":"Sportage"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":15705,"Model_Name":"Niro"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":21370,"Model_Name":"Stinger"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":25756,"Model_Name":"Telluride"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":26900,"Model_Name":"Seltos"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":27527,"Model_Name":"K5"},{"Make_ID":5848,"Make_Name":"MGS GRAND SPORT (MARDIKIAN)","Model_ID":15271,"Model_Name":"Miami"}]}
```
### vpic_Kia_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Kia/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:20:48Z | HTTP Date: Wed, 04 Nov 2026 12:20:49 GMT | Count: 13 | bytes: 1073
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":13,"Message":"Results returned successfully","SearchCriteria":"Make:Kia | ModelYear:2022","Results":[{"Make_ID":499,"Make_Name":"KIA","Model_ID":2299,"Model_Name":"Rio"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2460,"Model_Name":"Soul"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2462,"Model_Name":"Forte"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2769,"Model_Name":"Sorento"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2770,"Model_Name":"Sportage"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":15705,"Model_Name":"Niro"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":21370,"Model_Name":"Stinger"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":25756,"Model_Name":"Telluride"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":26900,"Model_Name":"Seltos"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":27527,"Model_Name":"K5"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":28294,"Model_Name":"Carnival"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":29462,"Model_Name":"EV6"},{"Make_ID":5848,"Make_Nam
```
### vpic_Kia_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Kia/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:20:50Z | HTTP Date: Wed, 04 Nov 2026 12:20:51 GMT | Count: 14 | bytes: 1151
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":14,"Message":"Results returned successfully","SearchCriteria":"Make:Kia | ModelYear:2023","Results":[{"Make_ID":499,"Make_Name":"KIA","Model_ID":2299,"Model_Name":"Rio"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2460,"Model_Name":"Soul"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2462,"Model_Name":"Forte"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2769,"Model_Name":"Sorento"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":2770,"Model_Name":"Sportage"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":15705,"Model_Name":"Niro"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":21370,"Model_Name":"Stinger"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":25756,"Model_Name":"Telluride"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":26900,"Model_Name":"Seltos"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":27527,"Model_Name":"K5"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":28294,"Model_Name":"Carnival"},{"Make_ID":499,"Make_Name":"KIA","Model_ID":29462,"Model_Name":"EV6"},{"Make_ID":5848,"Make_Nam
```
### vpic_Nissan_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Nissan/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:20:53Z | HTTP Date: Wed, 04 Nov 2026 12:20:53 GMT | Count: 28 | bytes: 2206
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":28,"Message":"Results returned successfully","SearchCriteria":"Make:Nissan | ModelYear:2021","Results":[{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1890,"Model_Name":"GT-R"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1890,"Model_Name":"GT-R"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1894,"Model_Name":"Versa"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1894,"Model_Name":"Versa"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1904,"Model_Name":"Altima"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1904,"Model_Name":"Altima"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1905,"Model_Name":"Leaf"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1905,"Model_Name":"Leaf"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1906,"Model_Name":"370Z"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1906,"Model_Name":"370Z"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1907,"Model_Name":"Sentra"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1907,"Model_Name":"Sentra"},{
```
### vpic_Nissan_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Nissan/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:20:56Z | HTTP Date: Wed, 04 Nov 2026 12:20:57 GMT | Count: 25 | bytes: 1990
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":25,"Message":"Results returned successfully","SearchCriteria":"Make:Nissan | ModelYear:2022","Results":[{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1890,"Model_Name":"GT-R"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1890,"Model_Name":"GT-R"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1894,"Model_Name":"Versa"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1894,"Model_Name":"Versa"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1904,"Model_Name":"Altima"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1904,"Model_Name":"Altima"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1905,"Model_Name":"Leaf"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1905,"Model_Name":"Leaf"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1906,"Model_Name":"370Z"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1906,"Model_Name":"370Z"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1907,"Model_Name":"Sentra"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1907,"Model_Name":"Sentra"},{
```
### vpic_Nissan_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Nissan/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:20:58Z | HTTP Date: Wed, 04 Nov 2026 12:20:59 GMT | Count: 16 | bytes: 1325
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":16,"Message":"Results returned successfully","SearchCriteria":"Make:Nissan | ModelYear:2023","Results":[{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1890,"Model_Name":"GT-R"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1894,"Model_Name":"Versa"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1904,"Model_Name":"Altima"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1905,"Model_Name":"Leaf"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1907,"Model_Name":"Sentra"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1911,"Model_Name":"Pathfinder"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1913,"Model_Name":"Rogue"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1914,"Model_Name":"Murano"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1915,"Model_Name":"Armada"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1918,"Model_Name":"NV200"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1919,"Model_Name":"Frontier"},{"Make_ID":478,"Make_Name":"NISSAN","Model_ID":1920,"Model_Name
```
### vpic_Ram_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ram/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:21:01Z | HTTP Date: Wed, 04 Nov 2026 12:21:01 GMT | Count: 111 | bytes: 9712
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":111,"Message":"Results returned successfully","SearchCriteria":"Make:Ram | ModelYear:2021","Results":[{"Make_ID":5686,"Make_Name":"BURKETT'S AUTORAMA","Model_ID":14901,"Model_Name":"Burkett's Autorama"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23261,"Model_Name":"CP90B"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23262,"Model_Name":"CP102B"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23263,"Model_Name":"CP80B"},{"Make_ID":1362,"Make_Name":"EASTON CUSTOM FRAMES L.L.C","Model_ID":4704,"Model_Name":"Easton Custom L.L.C"},{"Make_ID":6634,"Make_Name":"FATT HOGG FRAMES","Model_ID":17997,"Model_Name":"FATT HOGG FRAMES"},{"Make_ID":7116,"Make_Name":"FRAMTRAC MANUFACTURING CO. LTD","Model_ID":18958,"Model_Name":"FRAMTRAC MANUFACTURING CO. LTD"},{"Make_ID":2453,"Make_Name":"HOLIDAY RAMBLER","Model_ID":6265,"Model_Name":"Holiday Rambler"},{"Make_ID":11370,"Make_Name":"HOME GROWN CHOPPERS DBA FRAMED UP, LLC","Model_ID":29469,"Model_N
```
### vpic_Ram_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ram/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:21:03Z | HTTP Date: Wed, 04 Nov 2026 12:21:04 GMT | Count: 113 | bytes: 9884
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":113,"Message":"Results returned successfully","SearchCriteria":"Make:Ram | ModelYear:2022","Results":[{"Make_ID":5686,"Make_Name":"BURKETT'S AUTORAMA","Model_ID":14901,"Model_Name":"Burkett's Autorama"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23261,"Model_Name":"CP90B"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23262,"Model_Name":"CP102B"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23263,"Model_Name":"CP80B"},{"Make_ID":1362,"Make_Name":"EASTON CUSTOM FRAMES L.L.C","Model_ID":4704,"Model_Name":"Easton Custom L.L.C"},{"Make_ID":6634,"Make_Name":"FATT HOGG FRAMES","Model_ID":17997,"Model_Name":"FATT HOGG FRAMES"},{"Make_ID":11955,"Make_Name":"FRAMAR","Model_ID":30892,"Model_Name":"Framar"},{"Make_ID":7116,"Make_Name":"FRAMTRAC MANUFACTURING CO. LTD","Model_ID":18958,"Model_Name":"FRAMTRAC MANUFACTURING CO. LTD"},{"Make_ID":2453,"Make_Name":"HOLIDAY RAMBLER","Model_ID":6265,"Model_Name":"Holiday Rambler"},{"Make_ID":11370,
```
### vpic_Ram_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Ram/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:21:05Z | HTTP Date: Wed, 04 Nov 2026 12:21:06 GMT | Count: 113 | bytes: 9880
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":113,"Message":"Results returned successfully","SearchCriteria":"Make:Ram | ModelYear:2023","Results":[{"Make_ID":5686,"Make_Name":"BURKETT'S AUTORAMA","Model_ID":14901,"Model_Name":"Burkett's Autorama"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23261,"Model_Name":"CP90B"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23262,"Model_Name":"CP102B"},{"Make_ID":9049,"Make_Name":"CUSTOM WELDED FRAME","Model_ID":23263,"Model_Name":"CP80B"},{"Make_ID":1362,"Make_Name":"EASTON CUSTOM FRAMES L.L.C","Model_ID":4704,"Model_Name":"Easton Custom L.L.C"},{"Make_ID":6634,"Make_Name":"FATT HOGG FRAMES","Model_ID":17997,"Model_Name":"FATT HOGG FRAMES"},{"Make_ID":11955,"Make_Name":"FRAMAR","Model_ID":30892,"Model_Name":"Framar"},{"Make_ID":7116,"Make_Name":"FRAMTRAC MANUFACTURING CO. LTD","Model_ID":18958,"Model_Name":"FRAMTRAC MANUFACTURING CO. LTD"},{"Make_ID":2453,"Make_Name":"HOLIDAY RAMBLER","Model_ID":6265,"Model_Name":"Holiday Rambler"},{"Make_ID":11370,
```
### vpic_Subaru_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Subaru/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:21:07Z | HTTP Date: Wed, 04 Nov 2026 12:21:08 GMT | Count: 8 | bytes: 716
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":8,"Message":"Results returned successfully","SearchCriteria":"Make:Subaru | ModelYear:2021","Results":[{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2232,"Model_Name":"Legacy"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2233,"Model_Name":"Outback"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2234,"Model_Name":"Forester"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2235,"Model_Name":"Impreza"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2237,"Model_Name":"WRX"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2238,"Model_Name":"BRZ"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":13580,"Model_Name":"Crosstrek"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":24836,"Model_Name":"Ascent"}]}
```
### vpic_Subaru_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Subaru/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:21:08Z | HTTP Date: Wed, 04 Nov 2026 12:21:09 GMT | Count: 8 | bytes: 716
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":8,"Message":"Results returned successfully","SearchCriteria":"Make:Subaru | ModelYear:2022","Results":[{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2232,"Model_Name":"Legacy"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2233,"Model_Name":"Outback"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2234,"Model_Name":"Forester"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2235,"Model_Name":"Impreza"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2237,"Model_Name":"WRX"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2238,"Model_Name":"BRZ"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":13580,"Model_Name":"Crosstrek"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":24836,"Model_Name":"Ascent"}]}
```
### vpic_Subaru_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Subaru/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:21:10Z | HTTP Date: Wed, 04 Nov 2026 12:21:10 GMT | Count: 9 | bytes: 794
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":9,"Message":"Results returned successfully","SearchCriteria":"Make:Subaru | ModelYear:2023","Results":[{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2232,"Model_Name":"Legacy"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2233,"Model_Name":"Outback"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2234,"Model_Name":"Forester"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2235,"Model_Name":"Impreza"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2237,"Model_Name":"WRX"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":2238,"Model_Name":"BRZ"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":13580,"Model_Name":"Crosstrek"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":24836,"Model_Name":"Ascent"},{"Make_ID":523,"Make_Name":"SUBARU","Model_ID":30191,"Model_Name":"Solterra"}]}
```
### vpic_Toyota_2021
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Toyota/modelyear/2021?format=json`
- UTC time: 2026-11-04T12:21:11Z | HTTP Date: Wed, 04 Nov 2026 12:21:12 GMT | Count: 18 | bytes: 1495
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":18,"Message":"Results returned successfully","SearchCriteria":"Make:Toyota | ModelYear:2021","Results":[{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2208,"Model_Name":"Corolla"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2209,"Model_Name":"Prius"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2211,"Model_Name":"Land Cruiser"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2213,"Model_Name":"Highlander"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2216,"Model_Name":"4Runner"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2217,"Model_Name":"RAV4"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2223,"Model_Name":"Tacoma"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2465,"Model_Name":"Avalon"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2467,"Model_Name":"Tundra"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2468,"Model_Name":"Sienna"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2469,"Model_Name":"Camry"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2827,"M
```
### vpic_Toyota_2022
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Toyota/modelyear/2022?format=json`
- UTC time: 2026-11-04T12:21:13Z | HTTP Date: Wed, 04 Nov 2026 12:21:14 GMT | Count: 19 | bytes: 1571
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":19,"Message":"Results returned successfully","SearchCriteria":"Make:Toyota | ModelYear:2022","Results":[{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2208,"Model_Name":"Corolla"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2209,"Model_Name":"Prius"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2213,"Model_Name":"Highlander"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2216,"Model_Name":"4Runner"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2217,"Model_Name":"RAV4"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2223,"Model_Name":"Tacoma"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2465,"Model_Name":"Avalon"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2467,"Model_Name":"Tundra"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2468,"Model_Name":"Sienna"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2469,"Model_Name":"Camry"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2827,"Model_Name":"Sequoia"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":3005,"Model_
```
### vpic_Toyota_2023
- Request: `vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/Toyota/modelyear/2023?format=json`
- UTC time: 2026-11-04T12:21:14Z | HTTP Date: Wed, 04 Nov 2026 12:21:15 GMT | Count: 20 | bytes: 1651
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":20,"Message":"Results returned successfully","SearchCriteria":"Make:Toyota | ModelYear:2023","Results":[{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2208,"Model_Name":"Corolla"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2209,"Model_Name":"Prius"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2213,"Model_Name":"Highlander"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2216,"Model_Name":"4Runner"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2217,"Model_Name":"RAV4"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2223,"Model_Name":"Tacoma"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2467,"Model_Name":"Tundra"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2468,"Model_Name":"Sienna"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2469,"Model_Name":"Camry"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":2827,"Model_Name":"Sequoia"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":3005,"Model_Name":"Venza"},{"Make_ID":448,"Make_Name":"TOYOTA","Model_ID":3647,"Model_N
```
### probe_Chevrolet_Silverado_1500_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2021`
- UTC time: 2026-11-04T12:21:20Z | HTTP Date: Wed, 04 Nov 2026 12:21:20 GMT | Count: 855 | bytes: 883966
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":855,"message":"Results returned successfully","results":[{"odiNumber":11774360,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/12/2026","dateComplaintFiled":"10/29/2026","vin":"3GCPYFED9MG","components":"POWER TRAIN,ENGINE","summary":"The lifter on my cylinder one is failing. This is a known issue with the Chevrolet 5.3L 8cylinder engine and 2021 models are known for being notoriously bad with lifter issues. My safety and the safety of other drivers that own 2021 Chevrolet models is impacted due to this issue can cause the engine to completely fail and shut off while driving which could cause severe injuries up to death. The problem is a widespread issue and mine was confirmed by an independent service mechanic. The vehicle is now being inspected by the dealership. The issue did not arise until I reached 104,000 miles.","products":[{"type":"Vehicle","productYear":"2021","productMake":"CHEVROLET","prod
```
### recalls_Chevrolet_Silverado_1500_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2021`
- UTC time: 2026-11-04T12:21:29Z | HTTP Date: Wed, 04 Nov 2026 12:21:29 GMT | Count: 8 | bytes: 10880
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":8,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"20V792000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"17/12/2020","Component":"SEAT BELTS","Summary":"General Motors, LLC (GM) is recalling certain 2019-2021 Chevrolet Silverado 1500 and GMC Sierra 1500, 2021 Chevrolet Suburban and Tahoe and GMC Yukon XL and 2020-2021 Chevrolet Silverado 2500 and 3500 and GMC Sierra 2500 and 3500 vehicles.   The seat belt brackets may not be secured to the seat frame in the front-row center seating position.","Consequence":"If a seat-belt bracket is not secured, the seat belt may not properly restrain an occupant in the front-row center seat position, increasing the risk of injury in a crash.","Remedy":"GM will notify owners, and dealers will inspect left-side and right-side front-row center seat-belt bracket attachments and reassemble it correctly as necessary, free of charge.  The recall b
```
### complaints_Chevrolet_Silverado_1500_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2021`
- UTC time: 2026-11-04T12:21:34Z | HTTP Date: Wed, 04 Nov 2026 12:21:34 GMT | Count: 855 | bytes: 883966
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":855,"message":"Results returned successfully","results":[{"odiNumber":11774360,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/12/2026","dateComplaintFiled":"10/29/2026","vin":"3GCPYFED9MG","components":"POWER TRAIN,ENGINE","summary":"The lifter on my cylinder one is failing. This is a known issue with the Chevrolet 5.3L 8cylinder engine and 2021 models are known for being notoriously bad with lifter issues. My safety and the safety of other drivers that own 2021 Chevrolet models is impacted due to this issue can cause the engine to completely fail and shut off while driving which could cause severe injuries up to death. The problem is a widespread issue and mine was confirmed by an independent service mechanic. The vehicle is now being inspected by the dealership. The issue did not arise until I reached 104,000 miles.","products":[{"type":"Vehicle","productYear":"2021","productMake":"CHEVROLET","prod
```
### recalls_Chevrolet_Silverado_1500_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2022`
- UTC time: 2026-11-04T12:21:37Z | HTTP Date: Wed, 04 Nov 2026 12:21:37 GMT | Count: 6 | bytes: 8482
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":6,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"22V463000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"30/06/2022","Component":"EXTERIOR LIGHTING:BRAKE LIGHTS","Summary":"General Motors (GM) has decided that certain 2022 model year Chevrolet Silverado, and GMC Sierra vehicles equipped with an accessory sport bar.  The accessory sport bar contains a high-mounted brake light that may not function.  In addition, it may block the vehicle's existing high-mounted brake light.  As such, these vehicles may fail to conform to Federal Motor Vehicle Safety Standard (FMVSS) number 108, \"lamps, reflective devices, and associated equipment.\"","Consequence":"An inoperative high-mounted brake light can reduce visibility to other drivers and increase the risk of a crash.","Remedy":"Dealers will inspect the installation of the accessory bar and provide the correct vehicle wiring, if neces
```
### complaints_Chevrolet_Silverado_1500_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2022`
- UTC time: 2026-11-04T12:21:42Z | HTTP Date: Wed, 04 Nov 2026 12:21:42 GMT | Count: 656 | bytes: 671315
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":656,"message":"Results returned successfully","results":[{"odiNumber":11774479,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/30/2026","dateComplaintFiled":"10/29/2026","vin":"3gcpdbek6ng","components":"POWER TRAIN,FORWARD COLLISION AVOIDANCE","summary":"My vehicle has had numerous issues with electronics and cameras which have affected the ABS system. In addition to that there is a service bulletin for known issues of of the Rocker Arms failing which causes damage to the engine. While driving the vehicle no warning lights come on and the vehicle chugs and stops during driving which could cause a serious accident and injury. The rocker arms in this truck failed and cause further damage which has now caused the engine needing to be replaced at just 75,000 miles. GM service bulletins: PIP5847 & 25-NA-037","products":[{"type":"Vehicle","productYear":"2022","productMake":"CHEVROLET","productModel":"SILVE
```
### recalls_Chevrolet_Silverado_1500_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2023`
- UTC time: 2026-11-04T12:21:44Z | HTTP Date: Wed, 04 Nov 2026 12:21:45 GMT | Count: 3 | bytes: 4603
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"22V903000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":true,"ReportReceivedDate":"08/12/2022","Component":"EXTERIOR LIGHTING:LIGHTING CONTROL MODULE:SOFTWARE","Summary":"General Motors, LLC (GM) is recalling certain 2020-2023 Cadillac CT4 and CT5; 2021-2023 Buick Envision; and 2022-2023 Cadillac Escalade and Escalade ESV, Chevrolet Silverado 1500, Suburban, Tahoe, GMC Sierra 1500, Yukon, and Yukon XL vehicles.  The daytime running lights (DRLs) may not deactivate when the headlights are on.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 108, \"Lamps, Reflective Devices, and Associated Equipment.\"","Consequence":"DRLs that do not deactivate as intended may result in a glare, reducing visibility, and increasing the risk of a crash.","Remedy":"The body control module software will be updated b
```
### complaints_Chevrolet_Silverado_1500_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado%201500&modelYear=2023`
- UTC time: 2026-11-04T12:21:48Z | HTTP Date: Wed, 04 Nov 2026 12:21:48 GMT | Count: 391 | bytes: 432584
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":391,"message":"Results returned successfully","results":[{"odiNumber":11773622,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/22/2026","dateComplaintFiled":"10/26/2026","vin":"1gcudjel2pz","components":"SUSPENSION,POWER TRAIN,ENGINE","summary":"As I was exiting the exit ramp, you could here a noise from the suspension. Then a bunch of smoke came out and there truck seized up and stopped. I got out there was fluid/oil leaking everywhere. There was a trail of fluid following the car down the exit ramp.   The truck was telling me to restart but I didn't not due to safety concerns.  We had the car towed to the local Chevy dealership where it is being diagnose.  There were no warning lights prior or any notification that there was an issue.","products":[{"type":"Vehicle","productYear":"2023","productMake":"CHEVROLET","productModel":"SILVERADO 1500","manufacturer":"General Motors, LLC"}]},{"odiNumber":1177
```
### probe_Ram_1500_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ram&model=1500&modelYear=2021`
- UTC time: 2026-11-04T12:21:53Z | HTTP Date: Wed, 04 Nov 2026 12:21:53 GMT | Count: 686 | bytes: 696314
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":686,"message":"Results returned successfully","results":[{"odiNumber":11774477,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/06/2026","dateComplaintFiled":"10/29/2026","vin":"1c6srfft1mn","components":"ENGINE","summary":"The engine oil pan severely corroded and over 30% of the 18 gauge steel scaled away. For an 18-gauge steel oil pan (nominal thickness of 0.0478 inches or 1.2 mm), the threshold where rust becomes hazardous is remarkably thin—literally and figuratively. Because an oil pan holds hot, chemically active fluid and is subjected to constant vibration and thermal cycling, the margin for corrosion safety is very small: 1. The Pinhole and Leak Threshold (25% to 30% Loss)  * The Limit: If deep rust pitting or scaling eats away more than 0.012 to 0.015 inches (roughly 25% to 30% of the wall thickness), the metal is no longer structurally sound enough to contain the oil under thermal expans
```
### recalls_Ram_1500_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ram&model=1500&modelYear=2021`
- UTC time: 2026-11-04T12:21:55Z | HTTP Date: Wed, 04 Nov 2026 12:21:56 GMT | Count: 15 | bytes: 17743
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":15,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"21V438000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"10/06/2021","Component":"BACK OVER PREVENTION:DISPLAY FUNCTION","Summary":"Chrysler (FCA US, LLC) is recalling certain 2021 Ram 1500 vehicles equipped with a trailer reverse steering module (TRSCM).  The rearview camera image may not display.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 111, \"Rear Visibility.\"","Consequence":"A rearview camera that does not display an image reduces the driver's rear view, increasing the risk of a crash or injury.","Remedy":"Dealers will update the TRSCM software, free of charge.  Owner notification letters were mailed June 24, 2021.  Owners may contact FCA US, LLC customer service at 1-800-853-1403.  FCA, US, LLC's number for this recall is Y30.  This recall was supers
```
### complaints_Ram_1500_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ram&model=1500&modelYear=2021`
- UTC time: 2026-11-04T12:21:58Z | HTTP Date: Wed, 04 Nov 2026 12:21:58 GMT | Count: 686 | bytes: 696314
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":686,"message":"Results returned successfully","results":[{"odiNumber":11774477,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/06/2026","dateComplaintFiled":"10/29/2026","vin":"1c6srfft1mn","components":"ENGINE","summary":"The engine oil pan severely corroded and over 30% of the 18 gauge steel scaled away. For an 18-gauge steel oil pan (nominal thickness of 0.0478 inches or 1.2 mm), the threshold where rust becomes hazardous is remarkably thin—literally and figuratively. Because an oil pan holds hot, chemically active fluid and is subjected to constant vibration and thermal cycling, the margin for corrosion safety is very small: 1. The Pinhole and Leak Threshold (25% to 30% Loss)  * The Limit: If deep rust pitting or scaling eats away more than 0.012 to 0.015 inches (roughly 25% to 30% of the wall thickness), the metal is no longer structurally sound enough to contain the oil under thermal expans
```
### recalls_Ram_1500_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ram&model=1500&modelYear=2022`
- UTC time: 2026-11-04T12:22:02Z | HTTP Date: Wed, 04 Nov 2026 12:22:02 GMT | Count: 16 | bytes: 18777
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":16,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"21V871000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"10/11/2021","Component":"VISIBILITY:DEFROSTER/DEFOGGER/HVAC SYSTEM:WINDSHIELD:ELECTRICAL HEATING ELEMENT","Summary":"Chrysler (FCA US, LLC) is recalling certain 2022 Ram 1500 vehicles.  These vehicles may have been built with incompatible heating, ventilation, and air conditioning systems (HVAC), resulting in the windshield defrosting and defogging system being inoperable to drivers.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 103, \"Windshield Defrosting and Defogging Systems.\"","Consequence":"An inoperable defrosting and defogging system can reduce visibility for drivers in certain conditions, increasing the risk of a crash.","Remedy":"FCA US, LLC will repurchase the affected vehicles, free of charge
```
### complaints_Ram_1500_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ram&model=1500&modelYear=2022`
- UTC time: 2026-11-04T12:22:07Z | HTTP Date: Wed, 04 Nov 2026 12:22:08 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":0,"message":"Results returned successfully","results":[]}
```
### recalls_Ram_1500_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ram&model=1500&modelYear=2023`
- UTC time: 2026-11-04T12:22:10Z | HTTP Date: Wed, 04 Nov 2026 12:22:11 GMT | Count: 11 | bytes: 13830
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":11,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"23V059000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"09/02/2023","Component":"BACK OVER PREVENTION:DISPLAY FUNCTION","Summary":"Chrysler (FCA US, LLC) is recalling certain 2021-2023 Ram 1500 and 2023 Ram 2500 vehicles.  The trailer reverse steering control module (TRSCM) may prevent the rearview image from displaying when the vehicle is placed in reverse.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 111, \"Rear Visibility.\"","Consequence":"A rearview image that does not display while in reverse decreases the driver's visibility of the rear view, increasing the risk of injury or crash.","Remedy":"Dealers will update the TRSCM software, free of charge.  Owner notification letters were mailed March 1, 2023.  Owners may contact FCA US, LLC customer service at
```
### complaints_Ram_1500_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ram&model=1500&modelYear=2023`
- UTC time: 2026-11-04T12:22:17Z | HTTP Date: Wed, 04 Nov 2026 12:22:17 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":0,"message":"Results returned successfully","results":[]}
```
### probe_GMC_Sierra_1500_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra%201500&modelYear=2021`
- UTC time: 2026-11-04T12:22:23Z | HTTP Date: Wed, 04 Nov 2026 12:22:22 GMT | Count: 601 | bytes: 637794
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":601,"message":"Results returned successfully","results":[{"odiNumber":11774637,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/28/2026","dateComplaintFiled":"10/30/2026","vin":"3GTU9FELXMG","components":"STEERING,POWER TRAIN,ENGINE","summary":"The contact owns a 2021 GMC Sierra 1500. The contact stated that while driving 45 MPH, there was an abnormal knocking sound coming from the vehicle. The vehicle started hesitating, and there was a loss of power that became worse over time.  Additionally, the “Service Engine” and “Power Train” warning lights were illuminated. The messages “Loss of Steering Assist - Be Alert” and “Service Parking Brake” were displayed. The following day, the vehicle was driven in LIMP Mode to the dealer and was diagnosed with engine failure. The contact stated that there was an ongoing NHTSA investigation associated with the 6.2L engines. The failure mileage was ap
```
### recalls_GMC_Sierra_1500_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=GMC&model=Sierra%201500&modelYear=2021`
- UTC time: 2026-11-04T12:22:33Z | HTTP Date: Wed, 04 Nov 2026 12:22:34 GMT | Count: 7 | bytes: 9743
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":7,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"20V792000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"17/12/2020","Component":"SEAT BELTS","Summary":"General Motors, LLC (GM) is recalling certain 2019-2021 Chevrolet Silverado 1500 and GMC Sierra 1500, 2021 Chevrolet Suburban and Tahoe and GMC Yukon XL and 2020-2021 Chevrolet Silverado 2500 and 3500 and GMC Sierra 2500 and 3500 vehicles.   The seat belt brackets may not be secured to the seat frame in the front-row center seating position.","Consequence":"If a seat-belt bracket is not secured, the seat belt may not properly restrain an occupant in the front-row center seat position, increasing the risk of injury in a crash.","Remedy":"GM will notify owners, and dealers will inspect left-side and right-side front-row center seat-belt bracket attachments and reassemble it correctly as necessary, free of charge.  The recall b
```
### complaints_GMC_Sierra_1500_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra%201500&modelYear=2021`
- UTC time: 2026-11-04T12:22:38Z | HTTP Date: Wed, 04 Nov 2026 12:22:37 GMT | Count: 601 | bytes: 637794
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":601,"message":"Results returned successfully","results":[{"odiNumber":11774637,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/28/2026","dateComplaintFiled":"10/30/2026","vin":"3GTU9FELXMG","components":"STEERING,POWER TRAIN,ENGINE","summary":"The contact owns a 2021 GMC Sierra 1500. The contact stated that while driving 45 MPH, there was an abnormal knocking sound coming from the vehicle. The vehicle started hesitating, and there was a loss of power that became worse over time.  Additionally, the “Service Engine” and “Power Train” warning lights were illuminated. The messages “Loss of Steering Assist - Be Alert” and “Service Parking Brake” were displayed. The following day, the vehicle was driven in LIMP Mode to the dealer and was diagnosed with engine failure. The contact stated that there was an ongoing NHTSA investigation associated with the 6.2L engines. The failure mileage was ap
```
### recalls_GMC_Sierra_1500_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=GMC&model=Sierra%201500&modelYear=2022`
- UTC time: 2026-11-04T12:22:40Z | HTTP Date: Wed, 04 Nov 2026 12:22:41 GMT | Count: 6 | bytes: 8226
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":6,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"22V463000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"30/06/2022","Component":"EXTERIOR LIGHTING:BRAKE LIGHTS","Summary":"General Motors (GM) has decided that certain 2022 model year Chevrolet Silverado, and GMC Sierra vehicles equipped with an accessory sport bar.  The accessory sport bar contains a high-mounted brake light that may not function.  In addition, it may block the vehicle's existing high-mounted brake light.  As such, these vehicles may fail to conform to Federal Motor Vehicle Safety Standard (FMVSS) number 108, \"lamps, reflective devices, and associated equipment.\"","Consequence":"An inoperative high-mounted brake light can reduce visibility to other drivers and increase the risk of a crash.","Remedy":"Dealers will inspect the installation of the accessory bar and provide the correct vehicle wiring, if neces
```
### complaints_GMC_Sierra_1500_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra%201500&modelYear=2022`
- UTC time: 2026-11-04T12:22:46Z | HTTP Date: Wed, 04 Nov 2026 12:22:45 GMT | Count: 603 | bytes: 617269
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":603,"message":"Results returned successfully","results":[{"odiNumber":11774047,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/28/2026","dateComplaintFiled":"10/27/2026","vin":"1GTUUEET9NZ","components":"STRUCTURE","summary":"I was driving on a highway when the front grill deflector flew off of my vehicle and broke my driver's side windshield wiper. The incident scared me and made me jump and I'm not sure where the part went after it flew over my wind shield but it could have hit the car behind me. The part in question was part of recall 25V060. I took the vehicle to the dealership, and they said they had already completed the recall in June of 2025 and that GMC would not cover the cost of fixing it. I see there is a new query for this exact problem RQ26003.","products":[{"type":"Vehicle","productYear":"2022","productMake":"GMC","productModel":"SIERRA 1500","manufacturer":"General Motors, LLC"}]},{"od
```
### recalls_GMC_Sierra_1500_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=GMC&model=Sierra%201500&modelYear=2023`
- UTC time: 2026-11-04T12:22:50Z | HTTP Date: Wed, 04 Nov 2026 12:22:50 GMT | Count: 3 | bytes: 4576
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"22V903000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":true,"ReportReceivedDate":"08/12/2022","Component":"EXTERIOR LIGHTING:LIGHTING CONTROL MODULE:SOFTWARE","Summary":"General Motors, LLC (GM) is recalling certain 2020-2023 Cadillac CT4 and CT5; 2021-2023 Buick Envision; and 2022-2023 Cadillac Escalade and Escalade ESV, Chevrolet Silverado 1500, Suburban, Tahoe, GMC Sierra 1500, Yukon, and Yukon XL vehicles.  The daytime running lights (DRLs) may not deactivate when the headlights are on.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 108, \"Lamps, Reflective Devices, and Associated Equipment.\"","Consequence":"DRLs that do not deactivate as intended may result in a glare, reducing visibility, and increasing the risk of a crash.","Remedy":"The body control module software will be updated b
```
### complaints_GMC_Sierra_1500_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra%201500&modelYear=2023`
- UTC time: 2026-11-04T12:22:55Z | HTTP Date: Wed, 04 Nov 2026 12:22:54 GMT | Count: 507 | bytes: 524819
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":507,"message":"Results returned successfully","results":[{"odiNumber":11774611,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/01/2026","dateComplaintFiled":"10/30/2026","vin":"1GTUUHEL2PZ","components":"STRUCTURE","summary":"The contact owns a 2023 GMC Sierra 1500. While driving 70 MPH, the upper grille deflector detached and flew over the top of the vehicle. The vehicle was taken to the dealer, who determined that the upper grille deflector needed to be replaced. The contact associated the failure with NHTSA Action Number: RQ26003 (Structure). The manufacturer was notified of the failure by phone and advised the contact to report the failure to the NHTSA Hotline. The failure mileage was approximately 85,000.","products":[{"type":"Vehicle","productYear":"2023","productMake":"GMC","productModel":"SIERRA 1500","manufacturer":"General Motors, LLC"}]},{"odiNumber":11774342,"manufacturer":"General Motors,
```
### probe_Toyota_RAV4_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=RAV4&modelYear=2021`
- UTC time: 2026-11-04T12:23:00Z | HTTP Date: Wed, 04 Nov 2026 12:23:00 GMT | Count: 389 | bytes: 410607
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":389,"message":"Results returned successfully","results":[{"odiNumber":11772954,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/22/2026","dateComplaintFiled":"10/22/2026","vin":"2t3c1rfv0mw","components":"SERVICE BRAKES","summary":"I have had several intermittent occasions over the past 3-4 years where the brakes do not stop the vehicle when depressed. I can feel something through the brakes pedal, but cannot explain what it is. So far, I have been able to avoid any accidents, but the infrequency makes it impossible to determine if it is going to happen.","products":[{"type":"Vehicle","productYear":"2021","productMake":"TOYOTA","productModel":"RAV4","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11772670,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/01/2026","dateComplaintFiled":"10/21/2026","vin":"2T3H1
```
### recalls_Toyota_RAV4_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=RAV4&modelYear=2021`
- UTC time: 2026-11-04T12:23:04Z | HTTP Date: Wed, 04 Nov 2026 12:23:04 GMT | Count: 1 | bytes: 1488
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"23V865000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"20/12/2023","Component":"AIR BAGS:SENSOR:OCCUPANT CLASSIFICATION","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2020-2021 Avalon, Avalon Hybrid, Corolla, Highlander, Highlander Hybrid, RAV4, RAV4 Hybrid, Lexus ES350, Lexus RX350, Lexus RX450H, 2021 Sienna Hybrid, Lexus ES250, 2020-2022 Camry, Camry Hybrid, and ES300H vehicles.  A short circuit may develop in the Occupant Classification System (OCS) sensor, preventing the front passenger air bag from deploying.","Consequence":"An air bag that does not deploy during a crash increases the risk of injury.","Remedy":"Dealers will inspect and replace the sensor as necessary, free of charge.  Interim letters notifying owners of the safety risk were mailed in February 2024.
```
### complaints_Toyota_RAV4_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=RAV4&modelYear=2021`
- UTC time: 2026-11-04T12:23:11Z | HTTP Date: Wed, 04 Nov 2026 12:23:08 GMT | Count: 389 | bytes: 410607
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":389,"message":"Results returned successfully","results":[{"odiNumber":11772954,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/22/2026","dateComplaintFiled":"10/22/2026","vin":"2t3c1rfv0mw","components":"SERVICE BRAKES","summary":"I have had several intermittent occasions over the past 3-4 years where the brakes do not stop the vehicle when depressed. I can feel something through the brakes pedal, but cannot explain what it is. So far, I have been able to avoid any accidents, but the infrequency makes it impossible to determine if it is going to happen.","products":[{"type":"Vehicle","productYear":"2021","productMake":"TOYOTA","productModel":"RAV4","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11772670,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/01/2026","dateComplaintFiled":"10/21/2026","vin":"2T3H1
```
### recalls_Toyota_RAV4_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=RAV4&modelYear=2022`
- UTC time: 2026-11-04T12:23:12Z | HTTP Date: Wed, 04 Nov 2026 12:23:13 GMT | Count: 1 | bytes: 1420
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"22V519000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"21/07/2022","Component":"AIR BAGS:SENSOR:OCCUPANT CLASSIFICATION:FRONT PASSENGER","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2022 Rav4, Rav4 Hybrid, and Rav4 Prime vehicles.  The front passenger seat may have been assembled with interference between internal parts that may cause the Occupant Classification System (OCS) sensor to incorrectly detect the occupant.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 208, \"Occupant Crash Protection.\"","Consequence":"Incorrect detection of an occupant may result in improper air bag deployment during a crash, increasing the risk of injury.","Remedy":"Dealers will inspect and repair the front passenger seat, as 
```
### complaints_Toyota_RAV4_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=RAV4&modelYear=2022`
- UTC time: 2026-11-04T12:23:14Z | HTTP Date: Wed, 04 Nov 2026 12:23:15 GMT | Count: 150 | bytes: 155496
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":150,"message":"Results returned successfully","results":[{"odiNumber":11774811,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"07/16/2026","dateComplaintFiled":"10/31/2026","vin":"2T3W1RFV2NC","components":"ELECTRICAL SYSTEM,ENGINE","summary":"Re: Formal complaint — dealer billed for unperformed work, uncompleted Special Service Campaign 26TC03, $6,000 transmission quote with zero diagnostic codes, lifetime powertrain warranty not honored   On RAV4 stalled while I was driving. I brought it to the above dealer. The service advisor told me a sensor was replaced. It was not: the mass air flow sensor in the vehicle is dust-covered with inspection paint marks and is clearly not new (photo attached). Worse, the advisor's own TIS screenshot shows Special Service Campaign 26TC03 — Incorrect Mass Air Flow Sensor Reading — with Completion Status: NOT COMPLETED on my VIN. The campaign was never performed
```
### recalls_Toyota_RAV4_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=RAV4&modelYear=2023`
- UTC time: 2026-11-04T12:23:16Z | HTTP Date: Wed, 04 Nov 2026 12:23:17 GMT | Count: 3 | bytes: 4166
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"Gulf States Toyota, Inc.","NHTSACampaignNumber":"23V485000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"11/07/2023","Component":"TIRES:VALVE","Summary":"Gulf States Toyota, Inc. (GST) is recalling certain 2023 Toyota RAV4 vehicles equipped with 17\" black alloy accessory wheels.  During installation of the alloy wheels, the tire valve stem may have been improperly installed or damaged.  In addition, the load carrying capacity label may state the incorrect weight.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 110, \"Tire Selection and Rims.\"","Consequence":"A damaged or improperly installed valve stem may allow air to leak and/or the tires to be underinflated, increasing the risk of tire failure and a crash.","Remedy":"Dealers will inspect and, if necessary, replace the wheel valve stems and replace the lo
```
### complaints_Toyota_RAV4_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=RAV4&modelYear=2023`
- UTC time: 2026-11-04T12:23:18Z | HTTP Date: Wed, 04 Nov 2026 12:23:19 GMT | Count: 164 | bytes: 183875
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":164,"message":"Results returned successfully","results":[{"odiNumber":11773989,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/02/2026","dateComplaintFiled":"10/27/2026","vin":"4T3E6RFVXPU","components":"ELECTRICAL SYSTEM,VISIBILITY/WIPER","summary":"A 2023 Toyota RAV4 Hybrid XSE, purchased October 17, 2023, has experienced serious, recurring safety-related electronic failures for more than two years. The rearview backup camera intermittently displays a completely black image, even while other camera display functions remain operational. The multimedia/navigation screen also malfunctions or goes black while driving, causing navigation directions to disappear unexpectedly.  These failures create dangerous conditions. Loss of the backup camera compromises a critical safety feature when reversing, particularly around pedestrians and children. Unexpected display failures while driving can cause dange
```
### probe_Honda_CR_V_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=CR-V&modelYear=2021`
- UTC time: 2026-11-04T12:23:21Z | HTTP Date: Wed, 04 Nov 2026 12:23:22 GMT | Count: 341 | bytes: 360798
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":341,"message":"Results returned successfully","results":[{"odiNumber":11775200,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/22/2026","dateComplaintFiled":"11/02/2026","vin":"2HKRW2H59MH","components":"SERVICE BRAKES,FORWARD COLLISION AVOIDANCE","summary":"On the morning of Thursday, October 22, 2026, I was driving east through an intersection in Springfield, MO (where I had the green light and did not need to stop first), when the Automatic Emergency Braking system malfunctioned and slammed on the brakes.    Facing west, in the south-bound turn lane, was a truck at a full stop and NOT in my lane.  I believe this to be a dangerous malfunction of the Automatic Emergency Braking system. I was thankful that I was not rear-ended while stopped suddenly in the intersection.  That could have caused other collisions and resulting injury or death.  This was the first and only time that I have ex
```
### recalls_Honda_CR_V_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=CR-V&modelYear=2021`
- UTC time: 2026-11-04T12:23:22Z | HTTP Date: Wed, 04 Nov 2026 12:23:23 GMT | Count: 4 | bytes: 5384
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"21V900000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"18/11/2021","Component":"SEAT BELTS:REAR/OTHER:RETRACTOR","Summary":"Honda (American Honda Motor Co.) is recalling certain 2021 Accord Sedan, Accord Hybrid, CR-V, Ridgeline, 2022 Insight and CR-V Hybrid vehicles.  The automatic locking retractor on the second-row center seat belt assembly may deactivate improperly, which can result in an unsecured child restraint system.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 208, \"Occupant Crash Protection.\"","Consequence":"An unsecured child restraint system can increase the risk of injury during a crash.","Remedy":"Dealers will replace the second-row center seat belt assembly, free of charge.  Owner notification letters were mailed January 14, 2022.  
```
### complaints_Honda_CR_V_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=CR-V&modelYear=2021`
- UTC time: 2026-11-04T12:23:25Z | HTTP Date: Wed, 04 Nov 2026 12:23:25 GMT | Count: 341 | bytes: 360798
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":341,"message":"Results returned successfully","results":[{"odiNumber":11775200,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/22/2026","dateComplaintFiled":"11/02/2026","vin":"2HKRW2H59MH","components":"SERVICE BRAKES,FORWARD COLLISION AVOIDANCE","summary":"On the morning of Thursday, October 22, 2026, I was driving east through an intersection in Springfield, MO (where I had the green light and did not need to stop first), when the Automatic Emergency Braking system malfunctioned and slammed on the brakes.    Facing west, in the south-bound turn lane, was a truck at a full stop and NOT in my lane.  I believe this to be a dangerous malfunction of the Automatic Emergency Braking system. I was thankful that I was not rear-ended while stopped suddenly in the intersection.  That could have caused other collisions and resulting injury or death.  This was the first and only time that I have ex
```
### recalls_Honda_CR_V_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=CR-V&modelYear=2022`
- UTC time: 2026-11-04T12:23:26Z | HTTP Date: Wed, 04 Nov 2026 12:23:27 GMT | Count: 3 | bytes: 4064
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V524000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"27/07/2023","Component":"EQUIPMENT:OTHER:LABELS","Summary":"Honda (American Honda Motor Co.) is recalling certain 2017, 2020, and 2022 CR-V vehicles.  The certification label on the driver's side door states incorrect Gross Vehicle Weight Rating (GVWR), Gross Axle Weight Rating (GAWR), and tire size information.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 110, \"Tire Selection and Rims.\"","Consequence":"An incorrectly sized tire may cause premature tread wear, or a tire blow out, increasing the risk of a crash.","Remedy":"Dealers will install a new corrected label, free of charge.  Owner notification letters were mailed September 18, 2023.  Owners may contact Honda customer service at 1-888-23
```
### complaints_Honda_CR_V_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=CR-V&modelYear=2022`
- UTC time: 2026-11-04T12:23:29Z | HTTP Date: Wed, 04 Nov 2026 12:23:29 GMT | Count: 269 | bytes: 278168
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":269,"message":"Results returned successfully","results":[{"odiNumber":11773632,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/26/2026","dateComplaintFiled":"10/26/2026","vin":"5J6RT6H89NL","components":"VEHICLE SPEED CONTROL,ENGINE","summary":"Twice my 2022 Honda CR-V Hybrid lost power above 85 mph with a flashing check engine light: Restart recovery: Restarting restored normal operation. Check engine light: Flashed then went off after restart. Mileage: Over 100,000 miles.","products":[{"type":"Vehicle","productYear":"2022","productMake":"HONDA","productModel":"CR-V","manufacturer":"Honda (American Honda Motor Co.)"}]},{"odiNumber":11773108,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"02/12/2026","dateComplaintFiled":"10/22/2026","vin":"5J6RT6H89NL","components":"FUEL/PROPULSION SYSTEM","summary":"I
```
### recalls_Honda_CR_V_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=CR-V&modelYear=2023`
- UTC time: 2026-11-04T12:23:31Z | HTTP Date: Wed, 04 Nov 2026 12:23:31 GMT | Count: 3 | bytes: 3852
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V092000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"16/02/2023","Component":"SEATS:FRONT ASSEMBLY:RECLINER","Summary":"Honda (American Honda Motor Co.) is recalling certain 2023 CR-V vehicles.  The front passenger seat back frame may not have been welded properly, which can cause the seat back position to fail in the event of a crash.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard numbers 207, \"Seating Systems\" and 201, \"Occupant Protection in Interior Impact.\"","Consequence":"A seat back position that fails may not adequately restrain the occupant during a crash, increasing the risk of injury.","Remedy":"Dealers will replace the front passenger seat back frame assembly, free of charge.  Owner notification letters were mailed March 27, 2023.  Owners m
```
### complaints_Honda_CR_V_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=CR-V&modelYear=2023`
- UTC time: 2026-11-04T12:23:37Z | HTTP Date: Wed, 04 Nov 2026 12:23:37 GMT | Count: 517 | bytes: 509744
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":517,"message":"Results returned successfully","results":[{"odiNumber":11771683,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/01/2026","dateComplaintFiled":"10/16/2026","vin":"7FARS4H76PE","components":"STRUCTURE","summary":"The inner framework for the hood completely detached from the hood itself and very violently and aggressively shakes when the car is being driven on the highway or when it’s windy outside.","products":[{"type":"Vehicle","productYear":"2023","productMake":"HONDA","productModel":"CR-V","manufacturer":"Honda (American Honda Motor Co.)"}]},{"odiNumber":11770390,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/10/2026","dateComplaintFiled":"10/11/2026","vin":"7FARS6H54PE","components":"FORWARD COLLISION AVOIDANCE","summary":"The CMBS stopped working after the update was installed & 
```
### probe_Toyota_Camry_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Camry&modelYear=2021`
- UTC time: 2026-11-04T12:23:42Z | HTTP Date: Wed, 04 Nov 2026 12:23:42 GMT | Count: 158 | bytes: 145133
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":158,"message":"Results returned successfully","results":[{"odiNumber":11773787,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/30/2026","dateComplaintFiled":"10/26/2026","vin":"4T1G11AK6MU","components":"UNKNOWN OR OTHER","summary":"The door lock on passenger side does not engage or stay locked","products":[{"type":"Vehicle","productYear":"2021","productMake":"TOYOTA","productModel":"CAMRY","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11766822,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"02/10/2026","dateComplaintFiled":"09/24/2026","vin":"4T1KZ1AK1MU","components":"POWER TRAIN","summary":"I took it to a repair shop for a transmission issue, the technician noted the transmission fluid degraded or burnt fluid or And it is causing the torque converter shudder and transmission rpm to slip","products":[{"ty
```
### recalls_Toyota_Camry_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Camry&modelYear=2021`
- UTC time: 2026-11-04T12:23:46Z | HTTP Date: Wed, 04 Nov 2026 12:23:46 GMT | Count: 1 | bytes: 1489
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"23V865000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"20/12/2023","Component":"AIR BAGS:SENSOR:OCCUPANT CLASSIFICATION","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2020-2021 Avalon, Avalon Hybrid, Corolla, Highlander, Highlander Hybrid, RAV4, RAV4 Hybrid, Lexus ES350, Lexus RX350, Lexus RX450H, 2021 Sienna Hybrid, Lexus ES250, 2020-2022 Camry, Camry Hybrid, and ES300H vehicles.  A short circuit may develop in the Occupant Classification System (OCS) sensor, preventing the front passenger air bag from deploying.","Consequence":"An air bag that does not deploy during a crash increases the risk of injury.","Remedy":"Dealers will inspect and replace the sensor as necessary, free of charge.  Interim letters notifying owners of the safety risk were mailed in February 2024.
```
### complaints_Toyota_Camry_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Camry&modelYear=2021`
- UTC time: 2026-11-04T12:23:49Z | HTTP Date: Wed, 04 Nov 2026 12:23:49 GMT | Count: 158 | bytes: 145133
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":158,"message":"Results returned successfully","results":[{"odiNumber":11773787,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/30/2026","dateComplaintFiled":"10/26/2026","vin":"4T1G11AK6MU","components":"UNKNOWN OR OTHER","summary":"The door lock on passenger side does not engage or stay locked","products":[{"type":"Vehicle","productYear":"2021","productMake":"TOYOTA","productModel":"CAMRY","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11766822,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"02/10/2026","dateComplaintFiled":"09/24/2026","vin":"4T1KZ1AK1MU","components":"POWER TRAIN","summary":"I took it to a repair shop for a transmission issue, the technician noted the transmission fluid degraded or burnt fluid or And it is causing the torque converter shudder and transmission rpm to slip","products":[{"ty
```
### recalls_Toyota_Camry_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Camry&modelYear=2022`
- UTC time: 2026-11-04T12:23:52Z | HTTP Date: Wed, 04 Nov 2026 12:23:52 GMT | Count: 1 | bytes: 1489
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"23V865000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"20/12/2023","Component":"AIR BAGS:SENSOR:OCCUPANT CLASSIFICATION","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2020-2021 Avalon, Avalon Hybrid, Corolla, Highlander, Highlander Hybrid, RAV4, RAV4 Hybrid, Lexus ES350, Lexus RX350, Lexus RX450H, 2021 Sienna Hybrid, Lexus ES250, 2020-2022 Camry, Camry Hybrid, and ES300H vehicles.  A short circuit may develop in the Occupant Classification System (OCS) sensor, preventing the front passenger air bag from deploying.","Consequence":"An air bag that does not deploy during a crash increases the risk of injury.","Remedy":"Dealers will inspect and replace the sensor as necessary, free of charge.  Interim letters notifying owners of the safety risk were mailed in February 2024.
```
### complaints_Toyota_Camry_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Camry&modelYear=2022`
- UTC time: 2026-11-04T12:23:55Z | HTTP Date: Wed, 04 Nov 2026 12:23:55 GMT | Count: 65 | bytes: 66692
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":65,"message":"Results returned successfully","results":[{"odiNumber":11774112,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/27/2026","dateComplaintFiled":"10/27/2026","vin":"4T1K31AK1NU","components":"VISIBILITY/WIPER","summary":"The moonroof shattered as I was driving on a freeway. The shattering sounded like an explosion or gunshot sound that startled me resulting in some swerving in lanes. Traffic was light and I did not hit anything and was able to exit the freeway and pull into a gas station to examine what had happened. I noticed some glass falling from my car roof and saw that the moonroof was shattered.","products":[{"type":"Vehicle","productYear":"2022","productMake":"TOYOTA","productModel":"CAMRY","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11773958,"manufacturer":"Toyota Motor Corporation","crash":true,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident
```
### recalls_Toyota_Camry_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Camry&modelYear=2023`
- UTC time: 2026-11-04T12:23:57Z | HTTP Date: Wed, 04 Nov 2026 12:23:58 GMT | Count: 2 | bytes: 2475
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":2,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"23V432000","parkIt":true,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"15/06/2023","Component":"WHEELS:LUGS/NUTS/BOLTS/STUDS","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2023 Camry and Camry Hybrid vehicles.  The lug nuts that attach the wheels to the vehicle may be loose, which can result in wheel detachment.","Consequence":"A wheel that detaches from a moving vehicle can cause a loss of vehicle control, increasing the risk of a crash.","Remedy":"Owners are advised not to drive their vehicles until the repair has been performed.  Dealers will inspect and tighten the lug nuts, and replace any damaged components, free of charge.  Owner notification letters are expected to be mailed on or before August 14, 2023.  Owners may contact Toyota's customer service at 1-800-331-4331.  Toyota's 
```
### complaints_Toyota_Camry_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Camry&modelYear=2023`
- UTC time: 2026-11-04T12:24:01Z | HTTP Date: Wed, 04 Nov 2026 12:24:01 GMT | Count: 65 | bytes: 66482
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":65,"message":"Results returned successfully","results":[{"odiNumber":11771196,"manufacturer":"Toyota Motor Corporation","crash":true,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/03/2026","dateComplaintFiled":"10/14/2026","vin":"4T1G11BK6PU","components":"VEHICLE SPEED CONTROL","summary":"The contact owns a 2023 Toyota Camry. The contact stated that while attempting to exit the driveway at an undisclosed speed, the engine unexpectedly revved, and the vehicle accelerated forward, striking a trash bin. The contact stated that depressing the brake pedal caused the engine to rev higher. Upon shifting into Reverse (R), the vehicle unexpectedly accelerated at a high rate of speed, striking and knocking down three trees on the property. Depressing the brake pedal again while in reverse(R) similarly caused the engine to rev higher. The collisions resulted in heavy denting on all sides of the vehicle and significant undercarriage damage. The vehicle was towe
```
### probe_Nissan_Rogue_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Nissan&model=Rogue&modelYear=2021`
- UTC time: 2026-11-04T12:24:05Z | HTTP Date: Wed, 04 Nov 2026 12:24:05 GMT | Count: 295 | bytes: 310156
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":295,"message":"Results returned successfully","results":[{"odiNumber":11774324,"manufacturer":"Nissan North America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/26/2026","dateComplaintFiled":"10/28/2026","vin":"JN8AT3BA4MW","components":"ENGINE","summary":"I was driving when the engine stalled(the car jerked and then stopped) and the car came to a stop and automatically switched to park and then it turned off, after a few hours it started back up and the it was working ok until I got a message for Update fuel system and then qhen I was doing again it jerked","products":[{"type":"Vehicle","productYear":"2021","productMake":"NISSAN","productModel":"ROGUE","manufacturer":"Nissan North America, Inc."}]},{"odiNumber":11773780,"manufacturer":"Nissan North America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/05/2026","dateComplaintFiled":"10/26/2026","vin":"5N1AT3BA0MC","components":"A
```
### recalls_Nissan_Rogue_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Nissan&model=Rogue&modelYear=2021`
- UTC time: 2026-11-04T12:24:08Z | HTTP Date: Wed, 04 Nov 2026 12:24:09 GMT | Count: 10 | bytes: 11820
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":10,"Message":"Results returned successfully","results":[{"Manufacturer":"Nissan North America, Inc.","NHTSACampaignNumber":"21V957000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"09/12/2021","Component":"FUEL SYSTEM, GASOLINE:DELIVERY:FUEL PUMP","Summary":"Nissan North America, Inc. (Nissan) is recalling certain 2021 Rogue vehicles.  Abnormal wear inside the fuel pump may cause it to overheat and fail.","Consequence":"Fuel pump failure may cause an engine stall, increasing the risk of a crash.","Remedy":"Dealers will replace the fuel pump assembly, free of charge.  Owner notification letters were mailed January 27, 2022.  Owners may contact Nissan customer service at 1-800-867-7669.  Nissan's number for this recall is R21B8.","Notes":"Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.nhtsa.gov.","ModelYear":"2021","Make":"NISSAN","Model":"R
```
### complaints_Nissan_Rogue_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Nissan&model=Rogue&modelYear=2021`
- UTC time: 2026-11-04T12:24:12Z | HTTP Date: Wed, 04 Nov 2026 12:24:11 GMT | Count: 295 | bytes: 310156
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":295,"message":"Results returned successfully","results":[{"odiNumber":11774324,"manufacturer":"Nissan North America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/26/2026","dateComplaintFiled":"10/28/2026","vin":"JN8AT3BA4MW","components":"ENGINE","summary":"I was driving when the engine stalled(the car jerked and then stopped) and the car came to a stop and automatically switched to park and then it turned off, after a few hours it started back up and the it was working ok until I got a message for Update fuel system and then qhen I was doing again it jerked","products":[{"type":"Vehicle","productYear":"2021","productMake":"NISSAN","productModel":"ROGUE","manufacturer":"Nissan North America, Inc."}]},{"odiNumber":11773780,"manufacturer":"Nissan North America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/05/2026","dateComplaintFiled":"10/26/2026","vin":"5N1AT3BA0MC","components":"A
```
### recalls_Nissan_Rogue_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Nissan&model=Rogue&modelYear=2022`
- UTC time: 2026-11-04T12:24:15Z | HTTP Date: Wed, 04 Nov 2026 12:24:15 GMT | Count: 6 | bytes: 7264
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":6,"Message":"Results returned successfully","results":[{"Manufacturer":"Nissan North America, Inc.","NHTSACampaignNumber":"22V259000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"14/04/2022","Component":"FUEL SYSTEM, GASOLINE:STORAGE:TANK ASSEMBLY","Summary":"Nissan North America, Inc. (Nissan) is recalling certain 2022 Rogue vehicles.  Due to a manufacturing error, an area on the bottom wall of the fuel tank may be too thin.","Consequence":"Road debris may puncture the thin fuel tank wall, causing a gas leak and increasing the risk of a fire.  In addition, the fuel tank may not perform as expected during a crash, increasing the risk of injury.","Remedy":"Dealers will replace the fuel tank assembly and install a new lock ring, gasket, and o-ring seal, free of charge.  Owner notification letters were mailed May 19, 2022.  Owners may contact Nissan customer service at 1-800-867-7669.  Nissan's number for this recall is PC887.","Notes":"Owners
```
### complaints_Nissan_Rogue_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Nissan&model=Rogue&modelYear=2022`
- UTC time: 2026-11-04T12:24:18Z | HTTP Date: Wed, 04 Nov 2026 12:24:18 GMT | Count: 270 | bytes: 329560
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":270,"message":"Results returned successfully","results":[{"odiNumber":11774446,"manufacturer":"Nissan North America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/19/2026","dateComplaintFiled":"10/29/2026","vin":"5N1BT3BA6NC","components":"POWER TRAIN,ENGINE","summary":"An authorized Nissan franchise executed an active safety recall campaign on my vehicle regarding coolant loss. Technicians failed to secure critical powertrain components during reassembly. Three days post-delivery, a major engine bolt fell out on the highway and the chassis began vibrating violently. A certified military base auto hobby shop inspection officially grounded the vehicle, finding a broken rear motor mount bracket, unfastened structural bolts, and a completely disconnected transmission/engine hose left by the franchise. This constitutes a severe post-recall safety failure that actively endangered my family on public roads.","products":[{"type":"Vehicl
```
### recalls_Nissan_Rogue_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Nissan&model=Rogue&modelYear=2023`
- UTC time: 2026-11-04T12:24:19Z | HTTP Date: Wed, 04 Nov 2026 12:24:20 GMT | Count: 6 | bytes: 7641
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":6,"Message":"Results returned successfully","results":[{"Manufacturer":"Nissan North America, Inc.","NHTSACampaignNumber":"23V268000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"13/04/2023","Component":"SEATS:CRITICAL FASTENERS","Summary":"Nissan North America, Inc. (Nissan) is recalling certain 2023 Rogue, Pathfinder, and Infiniti QX60 vehicles.  The driver's powered seat may not be fully secured to the seat frame, causing the seat frame welds to detach from the rear inboard seat bracket.","Consequence":"An unsecured seat with broken welds may not properly restrain an occupant during a crash, increasing the risk of injury.","Remedy":"Dealers will inspect the driver's seat rail clearance, and if necessary, replace the driver's seat cushion frame, free of charge.  Owner notification letters are expected to be mailed June 10, 2023.  Owners may contact Nissan's customer service at 1-800-867-7669.  Nissan's number for this recall is PC966, PC9
```
### complaints_Nissan_Rogue_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Nissan&model=Rogue&modelYear=2023`
- UTC time: 2026-11-04T12:24:24Z | HTTP Date: Wed, 04 Nov 2026 12:24:25 GMT | Count: 766 | bytes: 853681
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":766,"message":"Results returned successfully","results":[{"odiNumber":11775018,"manufacturer":"Nissan North America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/31/2026","dateComplaintFiled":"11/01/2026","vin":"5N1BT3AB8PC","components":"POWER TRAIN,ENGINE","summary":"The vehicle suddenly lost power at Freeway speed and I had to pull over in traffic and then hobble to the next exit 45 mph which was the maximum speed I could reach. Then trying to get home on back roads I could barely accelerate through an intersection before the light turned red. It felt dangerous to even venture into the intersection because the power to accelerate was so incredibly low.","products":[{"type":"Vehicle","productYear":"2023","productMake":"NISSAN","productModel":"ROGUE","manufacturer":"Nissan North America, Inc."}]},{"odiNumber":11774815,"manufacturer":"Nissan North America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,
```
### probe_Chevrolet_Equinox_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Equinox&modelYear=2021`
- UTC time: 2026-11-04T12:24:27Z | HTTP Date: Wed, 04 Nov 2026 12:24:27 GMT | Count: 100 | bytes: 94845
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":100,"message":"Results returned successfully","results":[{"odiNumber":11771811,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/16/2026","dateComplaintFiled":"10/17/2026","vin":"3GNAXKEV1MS","components":"FUEL/PROPULSION SYSTEM","summary":"Vehicle engine \"sputtered\" last night on the roadway, made it home then car would not restart. Repair engine light warning came on at time vehicle engine \"sputtered\".  Vehicle will be at Dyer Chevrolet in Vero Beach, Florida on 10/19/2026.  Fuel  pump module is not providing fuel to engine resulting in engine not starting - See NHTSA Campaign  Number  23V013000","products":[{"type":"Vehicle","productYear":"2021","productMake":"CHEVROLET","productModel":"EQUINOX","manufacturer":"General Motors, LLC"}]},{"odiNumber":11770531,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/06/2026","dateCom
```
### recalls_Chevrolet_Equinox_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Equinox&modelYear=2021`
- UTC time: 2026-11-04T12:24:28Z | HTTP Date: Wed, 04 Nov 2026 12:24:29 GMT | Count: 4 | bytes: 5131
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"20V811000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"23/12/2020","Component":"SEAT BELTS","Summary":"General Motors, LLC (GM) is recalling certain 2020 Chevrolet Bolt EV and 2021 GMC Canyon and Sierra 1500, 2500 and 3500, Yukon, Yukon XL, Cadillac Escalade and Escalade ESV and Chevrolet Blazer, Camaro, Colorado, Equinox, Silverado 1500, 2500 and 3500, Suburban and Tahoe vehicles.  Incorrect bolts may have been used at one or more fastening locations to secure the seat belts to the vehicle.  If an incorrect bolt was used, the seat belt may not be properly attached to the vehicle.","Consequence":"If a seat belt assembly is not properly attached to the vehicle, the seat belt may not properly restrain an occupant in the event of a crash, increasing the risk of injury.","Remedy":"GM will notify owners, and dealers will replace t
```
### complaints_Chevrolet_Equinox_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Equinox&modelYear=2021`
- UTC time: 2026-11-04T12:24:30Z | HTTP Date: Wed, 04 Nov 2026 12:24:30 GMT | Count: 100 | bytes: 94845
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":100,"message":"Results returned successfully","results":[{"odiNumber":11771811,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/16/2026","dateComplaintFiled":"10/17/2026","vin":"3GNAXKEV1MS","components":"FUEL/PROPULSION SYSTEM","summary":"Vehicle engine \"sputtered\" last night on the roadway, made it home then car would not restart. Repair engine light warning came on at time vehicle engine \"sputtered\".  Vehicle will be at Dyer Chevrolet in Vero Beach, Florida on 10/19/2026.  Fuel  pump module is not providing fuel to engine resulting in engine not starting - See NHTSA Campaign  Number  23V013000","products":[{"type":"Vehicle","productYear":"2021","productMake":"CHEVROLET","productModel":"EQUINOX","manufacturer":"General Motors, LLC"}]},{"odiNumber":11770531,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/06/2026","dateCom
```
### recalls_Chevrolet_Equinox_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Equinox&modelYear=2022`
- UTC time: 2026-11-04T12:24:31Z | HTTP Date: Wed, 04 Nov 2026 12:24:32 GMT | Count: 5 | bytes: 5890
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":5,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"21V612000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"05/08/2021","Component":"TIRES","Summary":"General Motors, LLC (GM) is recalling certain 2021-2022 Chevrolet Equinox and GMC Terrain vehicles equipped with certain Hankook tires.  The tires may have been manufactured with an insufficient amount of curative agent, which could cause tread separation.","Consequence":"Tread separation can result in a loss of vehicle control, increasing the risk of a crash.","Remedy":"Dealers will inspect the tire DOT numbers, and replace any affected tires, free of charge.  Owner notification letters were mailed on August 31, 2021.  Owners may contact GMC customer service at 1-800-462-8782; and Chevrolet customer service at 1-800-222-1020.  GM's number for this recall is N212343560.","Notes":"Owners may also contact the National Highway Traff
```
### complaints_Chevrolet_Equinox_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Equinox&modelYear=2022`
- UTC time: 2026-11-04T12:24:34Z | HTTP Date: Wed, 04 Nov 2026 12:24:35 GMT | Count: 183 | bytes: 198394
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":183,"message":"Results returned successfully","results":[{"odiNumber":11774711,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/24/2026","dateComplaintFiled":"10/30/2026","vin":"3GNAXTEV8NL","components":"FUEL/PROPULSION SYSTEM","summary":"Hello,  I am writing regarding the fuel pump power control module failure in my 2022 Chevrolet Equinox LT.  On Thursday, XXX, my husband and I were left stranded at the intersection of [XXX]. While we were sitting at the intersection, my Equinox began to hesitate and then stopped completely. Although we could restart the vehicle, it would immediately shut off again. We had our emergency flashers on, but vehicles behind us continued honking whenever the light turned green. Being stranded in the middle of a busy highway was both humiliating and frightening.  VIN: [XXX]  After waiting approximately 1½ hours, a tow truck arrived and towed our vehicle to [XXX]. I was sub
```
### recalls_Chevrolet_Equinox_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Equinox&modelYear=2023`
- UTC time: 2026-11-04T12:24:37Z | HTTP Date: Wed, 04 Nov 2026 12:24:37 GMT | Count: 3 | bytes: 3869
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"22V724000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"29/09/2022","Component":"SEATS","Summary":"General Motors, LLC (GM) is recalling certain 2022-2023 Chevrolet Equinox and 2022 GMC Terrain vehicles.  The driver's seat may have a stripped or loose bolt at the seat frame height-adjust pivot.","Consequence":"A seat with a missing or loose bolt may not properly restrain the occupant in a crash, increasing the risk of injury.","Remedy":"Dealers will inspect the driver's seat and replace the seat cushion frame, if necessary, free of charge.  Owner notification letters were mailed on November 4, 2022.  Owners may contact Chevrolet customer service at 1-800-222-1020 or GMC customer service at 1-800-462-8782.  GMC's number for this recall is N222377890.","Notes":"Owners may also contact the National Highway Traffic Safety Administ
```
### complaints_Chevrolet_Equinox_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Equinox&modelYear=2023`
- UTC time: 2026-11-04T12:24:42Z | HTTP Date: Wed, 04 Nov 2026 12:24:42 GMT | Count: 99 | bytes: 102890
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":99,"message":"Results returned successfully","results":[{"odiNumber":11771568,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/14/2026","dateComplaintFiled":"10/16/2026","vin":"3GNAXUEG6PL","components":"POWER TRAIN,ELECTRICAL SYSTEM,ENGINE","summary":"Vehicle Safety Complaint — 2023 Chevrolet Equinox LT  I am reporting a potentially dangerous safety defect involving my 2023 Chevrolet Equinox LT equipped with the 1.5-liter turbocharged engine.  While operating my vehicle on a public roadway, it suddenly lost power and stopped functioning without advance warning, creating a dangerous situation for myself and other motorists. The vehicle had to be towed to an authorized Chevrolet dealership.  I received no prior recall notification, and my VIN did not indicate an applicable recall. The dealership informed me that the fuel pump recall applied only to 2.5-liter engines.  I am concerned because General Mo
```
### probe_Toyota_Tacoma_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Tacoma&modelYear=2021`
- UTC time: 2026-11-04T12:24:44Z | HTTP Date: Wed, 04 Nov 2026 12:24:44 GMT | Count: 81 | bytes: 80966
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":81,"message":"Results returned successfully","results":[{"odiNumber":11770043,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/13/2026","dateComplaintFiled":"10/09/2026","vin":"3TMCZ5AN0MM","components":"ENGINE","summary":"Engine developed a loud knock while under normal driving conditions at 61,000 miles. Oil was changed every 5k miles since new. Dealer says my oil rings on piston skirt have failed and heavy scoring on cylinder #5  Replaced short block under my aftermarket warranty. Toyota refused to cover it  because I was 1k miles over factory warranty","products":[{"type":"Vehicle","productYear":"2021","productMake":"TOYOTA","productModel":"TACOMA","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11762933,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"11/21/1981","dateComplaintFiled":"09/08/2026","vin":"3T
```
### recalls_Toyota_Tacoma_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Tacoma&modelYear=2021`
- UTC time: 2026-11-04T12:24:48Z | HTTP Date: Wed, 04 Nov 2026 12:24:49 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":0,"Message":"Results returned successfully","results":[]}
```
### complaints_Toyota_Tacoma_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Tacoma&modelYear=2021`
- UTC time: 2026-11-04T12:24:51Z | HTTP Date: Wed, 04 Nov 2026 12:24:52 GMT | Count: 81 | bytes: 80966
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":81,"message":"Results returned successfully","results":[{"odiNumber":11770043,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/13/2026","dateComplaintFiled":"10/09/2026","vin":"3TMCZ5AN0MM","components":"ENGINE","summary":"Engine developed a loud knock while under normal driving conditions at 61,000 miles. Oil was changed every 5k miles since new. Dealer says my oil rings on piston skirt have failed and heavy scoring on cylinder #5  Replaced short block under my aftermarket warranty. Toyota refused to cover it  because I was 1k miles over factory warranty","products":[{"type":"Vehicle","productYear":"2021","productMake":"TOYOTA","productModel":"TACOMA","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11762933,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"11/21/1981","dateComplaintFiled":"09/08/2026","vin":"3T
```
### recalls_Toyota_Tacoma_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Tacoma&modelYear=2022`
- UTC time: 2026-11-04T12:24:54Z | HTTP Date: Wed, 04 Nov 2026 12:24:54 GMT | Count: 3 | bytes: 3760
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"Gulf States Toyota, Inc.","NHTSACampaignNumber":"22V310000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"06/05/2022","Component":"EQUIPMENT:OTHER:LABELS","Summary":"Gulf States Toyota, Inc. (GST) is recalling certain 2022 4Runner, Tacoma, Highlander, and Highlander Hybrid vehicles.  The load carrying capacity modification labels may not be permanent and can fade, becoming illegible.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 110, \"Tire Selection and Rims.\"","Consequence":"An illegible label may allow the vehicle to be overloaded, increasing the risk of a crash.","Remedy":"GST will notify owners by mail, including a replacement load carrying capacity modification label for their vehicle and detailed replacement instructions, free of charge.  Owner notification letters were mailed June 30, 2022.  Owners 
```
### complaints_Toyota_Tacoma_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Tacoma&modelYear=2022`
- UTC time: 2026-11-04T12:24:56Z | HTTP Date: Wed, 04 Nov 2026 12:24:56 GMT | Count: 59 | bytes: 68526
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":59,"message":"Results returned successfully","results":[{"odiNumber":11766782,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"01/01/2024","dateComplaintFiled":"09/24/2026","vin":"3TMDZ5BN1NM","components":"STRUCTURE","summary":"2022 Tacoma paint peeling on all doors. Manufactured 1 months after current paint recall 23TE08 for 2016-2022 Tacomas. Quoted $7,000 for new paint job by Maita Toyota in Sacramento Ca and Toyota Corp only offered me $2500, which I declined. This is stupid!","products":[{"type":"Vehicle","productYear":"2022","productMake":"TOYOTA","productModel":"TACOMA","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11764832,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/01/2026","dateComplaintFiled":"09/16/2026","vin":"3TMCZ5AN6NM","components":"FUEL/PROPULSION SYSTEM","summary":"Car has difficulty 
```
### recalls_Toyota_Tacoma_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Tacoma&modelYear=2023`
- UTC time: 2026-11-04T12:29:20Z | HTTP Date: Wed, 04 Nov 2026 12:29:22 GMT | Count: 4 | bytes: 5490
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"22V520000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"21/07/2022","Component":"CHILD SEAT:VEHICLE LATCH ANCHOR","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2022-2023 Tacoma vehicles.  One or more of the individual welds in the upper child seat anchors may be insufficient.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 225, \"Child Restraint Anchorage System.\"","Consequence":"An insufficient weld may prevent the child seat from being anchored properly, allowing the seat to move during a sudden stop or crash, increasing the risk of injury.","Remedy":"Dealers will inspect the upper child seat anchors and reweld the child seat anchors, as necessary.  Owner notification letters are expected to be mailed Septe
```
### complaints_Toyota_Tacoma_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Tacoma&modelYear=2023`
- UTC time: 2026-11-04T12:29:22Z | HTTP Date: Wed, 04 Nov 2026 12:29:25 GMT | Count: 54 | bytes: 62403
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":54,"message":"Results returned successfully","results":[{"odiNumber":11763071,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/25/2026","dateComplaintFiled":"09/09/2026","vin":"3TYCZ5AN4PT","components":"ELECTRICAL SYSTEM,LANE DEPARTURE","summary":"Check BSM light came on Dealer found chafed wiring harness","products":[{"type":"Vehicle","productYear":"2023","productMake":"TOYOTA","productModel":"TACOMA","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11760451,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/28/2026","dateComplaintFiled":"08/28/2026","vin":"3tmcz5an8pm","components":"VEHICLE SPEED CONTROL","summary":"After initial start of engine and at idle there is surge of the engine and lunge forward while in drive. The danger is unexpected forward movement of the truck when pulling forward at idle by lun
```
### probe_Honda_Civic_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Civic&modelYear=2021`
- UTC time: 2026-11-04T12:30:01Z | HTTP Date: Wed, 04 Nov 2026 12:30:05 GMT | Count: 148 | bytes: 134660
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":148,"message":"Results returned successfully","results":[{"odiNumber":11774591,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/04/2026","dateComplaintFiled":"10/30/2026","vin":"2HGFC2F67MH","components":"STEERING","summary":"“My 2021 Honda Civic experiences intermittent steering resistance. At approximately 0- plus speed, the steering feels sticky at or near TDC of the steering wheel, requiring a little nudge. to correct it. It occurs frequent during warm and/or humid conditions. The vehicle has approximately 81,000 miles. I just bought it so I don't know how long this has been happening in the past years. I will be training my son to drive in this car. So, I worry of it getting stuck. The dealer has not inspected the vehicle yet because they charge for the check.?","products":[{"type":"Vehicle","productYear":"2021","productMake":"HONDA","productModel":"CIVIC","manufacturer":"Honda (Ame
```
### recalls_Honda_Civic_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Civic&modelYear=2021`
- UTC time: 2026-11-04T12:30:04Z | HTTP Date: Wed, 04 Nov 2026 12:30:08 GMT | Count: 4 | bytes: 5431
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V458000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"29/06/2023","Component":"SERVICE BRAKES, HYDRAULIC:FOUNDATION COMPONENTS:MASTER CYLINDER","Summary":"Honda (American Honda Motor Co.) is recalling certain 2020-2021 Civic, 2020-2023 Ridgeline, 2021-2023 Passport, 2021-2022 Pilot, and 2020 Acura MDX vehicles.  The tie rod fastener that connects the brake booster and the brake master cylinder may have been improperly assembled during manufacturing, which can cause the brake master cylinder to separate from the booster assembly.","Consequence":"Brake master cylinder separation can cause a loss of brake function and increase the risk of a crash.","Remedy":"Dealers will inspect and repair the brake booster assembly as necessary, free of charge.  Owner notification letters were mailed August 7, 2023.  Owners may co
```
### complaints_Honda_Civic_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Civic&modelYear=2021`
- UTC time: 2026-11-04T12:30:07Z | HTTP Date: Wed, 04 Nov 2026 12:30:11 GMT | Count: 148 | bytes: 134660
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":148,"message":"Results returned successfully","results":[{"odiNumber":11774591,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/04/2026","dateComplaintFiled":"10/30/2026","vin":"2HGFC2F67MH","components":"STEERING","summary":"“My 2021 Honda Civic experiences intermittent steering resistance. At approximately 0- plus speed, the steering feels sticky at or near TDC of the steering wheel, requiring a little nudge. to correct it. It occurs frequent during warm and/or humid conditions. The vehicle has approximately 81,000 miles. I just bought it so I don't know how long this has been happening in the past years. I will be training my son to drive in this car. So, I worry of it getting stuck. The dealer has not inspected the vehicle yet because they charge for the check.?","products":[{"type":"Vehicle","productYear":"2021","productMake":"HONDA","productModel":"CIVIC","manufacturer":"Honda (Ame
```
### recalls_Honda_Civic_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Civic&modelYear=2022`
- UTC time: 2026-11-04T12:30:10Z | HTTP Date: Wed, 04 Nov 2026 12:30:13 GMT | Count: 4 | bytes: 5266
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V704000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"19/10/2023","Component":"STEERING:RACK AND PINION","Summary":"Honda (American Honda Motor Co.) is recalling certain 2022-2024 Civic 4-door and Civic 5-door vehicles that received a replacement power steering rack as part of a service repair.  The steering rack may have been incorrectly assembled, which can allow the tire to chafe against the lower suspension or tie rod end, possibly resulting in tire damage.","Consequence":"A damaged tire can fail and increase the risk of a crash or injury.","Remedy":"Dealers will inspect and replace the electric power steering rack, as necessary, free of charge.  Owner letters were mailed January 16, 2024.  Owners may contact Honda customer service at 1-888-234-2138.  Honda's number for this recall is YFW.","Notes":"Owners m
```
### complaints_Honda_Civic_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Civic&modelYear=2022`
- UTC time: 2026-11-04T12:30:13Z | HTTP Date: Wed, 04 Nov 2026 12:30:17 GMT | Count: 886 | bytes: 832076
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":886,"message":"Results returned successfully","results":[{"odiNumber":11773965,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/24/2026","dateComplaintFiled":"10/27/2026","vin":"2HGFE2F5XNH","components":"STEERING","summary":"The contact owns a 2022 Honda Civic. The contact stated that the vehicle was previously repaired under NHTSA Campaign Number: 23V704000 (Steering); however, the failure occurred a year after the recall repair. While driving at approximately 45-70 MPH, the steering wheel was sticking. The vehicle was taken to the dealer, who determined that the rack and pinion needed to be replaced. The manufacturer was notified of the failure by email. The failure mileage was approximately 84,300.","products":[{"type":"Vehicle","productYear":"2022","productMake":"HONDA","productModel":"CIVIC","manufacturer":"Honda (American Honda Motor Co.)"}]},{"odiNumber":11771164,"manufacturer":"Ho
```
### recalls_Honda_Civic_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Civic&modelYear=2023`
- UTC time: 2026-11-04T12:30:17Z | HTTP Date: Wed, 04 Nov 2026 12:30:20 GMT | Count: 4 | bytes: 4923
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V430000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"15/06/2023","Component":"SERVICE BRAKES, HYDRAULIC:ANTILOCK/TRACTION CONTROL/ELECTRONIC LIMITED SLIP:CONTROL UNIT/MODULE","Summary":"Honda (America Honda Motor Co.) is recalling certain 2023 Civic, Acura RDX, Acura Integra, and 2022 Honda Accord vehicles.  A ball valve in the vehicle stability assist (VSA) modulator may leak brake fluid, which can result in unintended vehicle movement when the brake hold feature is engaged or an unexpected increase in brake pedal travel.","Consequence":"Unintended vehicle movement or an unexpected increase in brake pedal travel can increase the risk of a crash or injury.","Remedy":"Dealers will replace the VSA modulator, free of charge.  Owner notification letters were mailed July 24, 2023.  Owners may contact Honda customer 
```
### complaints_Honda_Civic_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Civic&modelYear=2023`
- UTC time: 2026-11-04T12:30:19Z | HTTP Date: Wed, 04 Nov 2026 12:30:23 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":0,"message":"Results returned successfully","results":[]}
```
### probe_Honda_Accord_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Accord&modelYear=2021`
- UTC time: 2026-11-04T12:30:22Z | HTTP Date: Wed, 04 Nov 2026 12:30:27 GMT | Count: 246 | bytes: 256111
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":246,"message":"Results returned successfully","results":[{"odiNumber":11774309,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/30/2025","dateComplaintFiled":"10/28/2026","vin":"1HGCV1F11MA","components":"ENGINE,FUEL/PROPULSION SYSTEM,LANE DEPARTURE","summary":"I am submitting this complaint regarding an ongoing safety concern with my 2021 Honda Accord. Multiple lights indicate engine system problems which includes, check engine light, car jerks at acceleration, seat sensor recall. I took my vehicle to multiple shops including the Honda Dealership. However, they were unsuccessful to identify the cause. Multiple problems such as Turbo, belt, fuel system problem constantly comes up. I have attempted to take my vehicle for the recall, which was scheduled, however after waiting 4hrs, the dealership stated they did not have the parts. I am concerned about the potential risk to myself, my daught
```
### recalls_Honda_Accord_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Accord&modelYear=2021`
- UTC time: 2026-11-04T12:30:26Z | HTTP Date: Wed, 04 Nov 2026 12:30:30 GMT | Count: 4 | bytes: 5392
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"21V900000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"18/11/2021","Component":"SEAT BELTS:REAR/OTHER:RETRACTOR","Summary":"Honda (American Honda Motor Co.) is recalling certain 2021 Accord Sedan, Accord Hybrid, CR-V, Ridgeline, 2022 Insight and CR-V Hybrid vehicles.  The automatic locking retractor on the second-row center seat belt assembly may deactivate improperly, which can result in an unsecured child restraint system.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 208, \"Occupant Crash Protection.\"","Consequence":"An unsecured child restraint system can increase the risk of injury during a crash.","Remedy":"Dealers will replace the second-row center seat belt assembly, free of charge.  Owner notification letters were mailed January 14, 2022.  
```
### complaints_Honda_Accord_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Accord&modelYear=2021`
- UTC time: 2026-11-04T12:30:30Z | HTTP Date: Wed, 04 Nov 2026 12:30:34 GMT | Count: 246 | bytes: 256111
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":246,"message":"Results returned successfully","results":[{"odiNumber":11774309,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/30/2025","dateComplaintFiled":"10/28/2026","vin":"1HGCV1F11MA","components":"ENGINE,FUEL/PROPULSION SYSTEM,LANE DEPARTURE","summary":"I am submitting this complaint regarding an ongoing safety concern with my 2021 Honda Accord. Multiple lights indicate engine system problems which includes, check engine light, car jerks at acceleration, seat sensor recall. I took my vehicle to multiple shops including the Honda Dealership. However, they were unsuccessful to identify the cause. Multiple problems such as Turbo, belt, fuel system problem constantly comes up. I have attempted to take my vehicle for the recall, which was scheduled, however after waiting 4hrs, the dealership stated they did not have the parts. I am concerned about the potential risk to myself, my daught
```
### recalls_Honda_Accord_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Accord&modelYear=2022`
- UTC time: 2026-11-04T12:30:34Z | HTTP Date: Wed, 04 Nov 2026 12:30:39 GMT | Count: 4 | bytes: 5423
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V430000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"15/06/2023","Component":"SERVICE BRAKES, HYDRAULIC:ANTILOCK/TRACTION CONTROL/ELECTRONIC LIMITED SLIP:CONTROL UNIT/MODULE","Summary":"Honda (America Honda Motor Co.) is recalling certain 2023 Civic, Acura RDX, Acura Integra, and 2022 Honda Accord vehicles.  A ball valve in the vehicle stability assist (VSA) modulator may leak brake fluid, which can result in unintended vehicle movement when the brake hold feature is engaged or an unexpected increase in brake pedal travel.","Consequence":"Unintended vehicle movement or an unexpected increase in brake pedal travel can increase the risk of a crash or injury.","Remedy":"Dealers will replace the VSA modulator, free of charge.  Owner notification letters were mailed July 24, 2023.  Owners may contact Honda customer 
```
### complaints_Honda_Accord_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Accord&modelYear=2022`
- UTC time: 2026-11-04T12:30:38Z | HTTP Date: Wed, 04 Nov 2026 12:30:43 GMT | Count: 262 | bytes: 281077
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":262,"message":"Results returned successfully","results":[{"odiNumber":11774472,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/17/2026","dateComplaintFiled":"10/29/2026","vin":"1hgcv3f23na","components":"ELECTRICAL SYSTEM","summary":"The Center Display Audio / Infotainment Touchscreen unit continuously fails. The component is available for inspection upon request, as it remains installed in the vehicle in its malfunctioning state.  Safety severely compromised due to extreme driver distraction caused by the unit erratically flashing, cycling through menus, and emitting continuous, loud audible beeps while operating the vehicle in active traffic. Additionally, the malfunction regularly causes the screen to freeze, completely disabling the rearview backup camera display and preventing the visual display of critical advanced driver-assist safety alerts.  Yes. The failure was officially reprod
```
### probe_Ford_Escape_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Escape&modelYear=2021`
- UTC time: 2026-11-04T12:34:43Z | HTTP Date: Wed, 04 Nov 2026 12:35:28 GMT | Count: 355 | bytes: 324934
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":355,"message":"Results returned successfully","results":[{"odiNumber":11775244,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/30/2026","dateComplaintFiled":"11/02/2026","vin":"1FMCU9BZ7MU","components":"ENGINE","summary":"Car is experiencing internal engine component deterioration under Recall 23S27. Auffenberg Ford in O'Fallon, IL cleared the critical P1061 safety code on October 6 using my code reader, saying they didn’t have time to hook it up to their system and sent me home with an appointment to bring it back in, without fixing the vehicle. Ford Corporate is now utilizing that unauthorized deletion to deny my engine replacement under Customer Satisfaction Program 23N06, forcing me to drive a vehicle with a documented catastrophic engine failure and fire risk until it either throws the code again or catches fire, possibly killing one of my children, or throws a rod.","products":[{"type":"Vehicl
```
### recalls_Ford_Escape_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Escape&modelYear=2021`
- UTC time: 2026-11-04T12:35:28Z | HTTP Date: Wed, 04 Nov 2026 12:35:31 GMT | Count: 19 | bytes: 23200
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":19,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"21V869000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"10/11/2021","Component":"ELECTRICAL SYSTEM:PROPULSION SYSTEM:TRACTION BATTERY","Summary":"Ford Motor Company (Ford) is recalling one 2021 Escape vehicle equipped with a 2.5L hybrid powertrain.  The high voltage battery may fail, resulting in a sudden loss of drive power.","Consequence":"A sudden loss of drive power increases the risk of a crash.","Remedy":"A dealer will replace the high voltage battery, free of charge.  The owner notification letters were mailed December 1, 2021.  Owners may contact Ford customer service at 1-866-436-7332.  Ford's number for this recall is 21S48.","Notes":"Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.nhtsa.gov.","ModelYear":"2021","Ma
```
### complaints_Ford_Escape_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Escape&modelYear=2021`
- UTC time: 2026-11-04T12:35:31Z | HTTP Date: Wed, 04 Nov 2026 12:35:36 GMT | Count: 355 | bytes: 324934
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":355,"message":"Results returned successfully","results":[{"odiNumber":11775244,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/30/2026","dateComplaintFiled":"11/02/2026","vin":"1FMCU9BZ7MU","components":"ENGINE","summary":"Car is experiencing internal engine component deterioration under Recall 23S27. Auffenberg Ford in O'Fallon, IL cleared the critical P1061 safety code on October 6 using my code reader, saying they didn’t have time to hook it up to their system and sent me home with an appointment to bring it back in, without fixing the vehicle. Ford Corporate is now utilizing that unauthorized deletion to deny my engine replacement under Customer Satisfaction Program 23N06, forcing me to drive a vehicle with a documented catastrophic engine failure and fire risk until it either throws the code again or catches fire, possibly killing one of my children, or throws a rod.","products":[{"type":"Vehicl
```
### recalls_Ford_Escape_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Escape&modelYear=2022`
- UTC time: 2026-11-04T12:35:35Z | HTTP Date: Wed, 04 Nov 2026 12:35:43 GMT | Count: 19 | bytes: 23381
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":19,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"21V922000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"24/11/2021","Component":"SERVICE BRAKES, HYDRAULIC:FOUNDATION COMPONENTS:DISC:CALIPER","Summary":"Ford Motor Company (Ford) is recalling certain 2021-2022 Bronco Sport and Escape vehicles.  The rear brake linings may have been manufactured incorrectly, which can affect braking performance.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 135, \"Light Vehicle Brake Systems.\"","Consequence":"During certain situations, the driver may have to apply more brake pedal force, and the distance required to stop the vehicle may be extended, increasing the risk of a crash.","Remedy":"Dealers will replace the front brake pads, free of charge.   Owner notification letters were mailed August 17, 2022.  Owners may contact Ford
```
### complaints_Ford_Escape_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Escape&modelYear=2022`
- UTC time: 2026-11-04T12:35:43Z | HTTP Date: Wed, 04 Nov 2026 12:35:47 GMT | Count: 238 | bytes: 233906
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":238,"message":"Results returned successfully","results":[{"odiNumber":11774820,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/09/2026","dateComplaintFiled":"10/31/2026","vin":"1FMCU9G66NU","components":"ELECTRICAL SYSTEM,UNKNOWN OR OTHER,ENGINE","summary":"In early XXX, my 2022 Ford Escape SE (1.5L EcoBoost) experienced repeated engine stalls while my wife was driving with our children inside. The vehicle had only 33,028 miles. Whenever the A/C was engaged, the engine stalled and could not restart normally until the A/C was turned off. With the A/C off, the vehicle could restart and drive. Turning the A/C back on caused the engine to stall again. A strong burning/electrical smell accompanied the malfunction and persisted even with the A/C off.  The failure occurred suddenly, without prior symptoms. Whether dashboard warning lights appeared is UNKNOWN. Losing engine power while driving created a seriou
```
### recalls_Ford_Escape_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Escape&modelYear=2023`
- UTC time: 2026-11-04T12:35:47Z | HTTP Date: Wed, 04 Nov 2026 12:35:52 GMT | Count: 11 | bytes: 14276
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":11,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"22V859000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"19/11/2022","Component":"FUEL SYSTEM, GASOLINE:FUEL INJECTION SYSTEM","Summary":"Ford Motor Company (Ford) is recalling certain 2020-2023 Escape and 2021-2023 Bronco Sport vehicles equipped with 1.5L engines.  A fuel injector may crack and leak fuel inside the engine compartment.","Consequence":"A fuel leak in the presence of an ignition source such as hot engine or exhaust components, can increase the risk of a fire.","Remedy":"Dealers will update the engine control software to include fuel injector leak detection and install a drain tube, free of charge.  Interim owner notification letters informing owners of the safety risk were mailed January 9, 2023.  Remedy parts are expected to be available in 1st Quarter of 2023.   Owner notification letters were mailed February 2
```
### complaints_Ford_Escape_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Escape&modelYear=2023`
- UTC time: 2026-11-04T12:35:52Z | HTTP Date: Wed, 04 Nov 2026 12:35:57 GMT | Count: 102 | bytes: 109300
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":102,"message":"Results returned successfully","results":[{"odiNumber":11773832,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/26/2026","dateComplaintFiled":"10/26/2026","vin":"1FMCU9FN9PU","components":"POWER TRAIN","summary":"I was driving to work and the transmission faltered, grinded, tried to shift, and I thought the vehicle was going to crash. There were cars around me, and I was going about 30 to 35 miles per hour. I was able to pull over and turned off the car. I then drove it to an auto shop and the mechanic stated that it is the transmission. My Ford Escape 2023 has 68,000 miles. It has stalled twice on the road at a stop light/stop sign since August 2026 also. I no longer trust that the vehicle is safe.","products":[{"type":"Vehicle","productYear":"2023","productMake":"FORD","productModel":"ESCAPE","manufacturer":"Ford Motor Company"}]},{"odiNumber":11772431,"manufacturer":"Ford Motor Compan
```
### probe_Toyota_Corolla_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Corolla&modelYear=2021`
- UTC time: 2026-11-04T12:35:56Z | HTTP Date: Wed, 04 Nov 2026 12:36:01 GMT | Count: 188 | bytes: 181704
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":188,"message":"Results returned successfully","results":[{"odiNumber":11772907,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"05/01/2024","dateComplaintFiled":"10/22/2026","vin":"5YFS4MCE7MP","components":"WHEELS,UNKNOWN OR OTHER","summary":"Front wheel bearings   my vehicle has 63,000 my front right wheel bearing changed at 32,000 - now I need both front wheel bearing replaced","products":[{"type":"Vehicle","productYear":"2021","productMake":"TOYOTA","productModel":"COROLLA","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11772448,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"05/22/2026","dateComplaintFiled":"10/20/2026","vin":"5yfepmae1mp","components":"AIR BAGS","summary":"On May 22, 2026, I got off work and started my 2021 Toyota Corolla LE when I noticed the SRS airbag warning light was on. The warning l
```
### recalls_Toyota_Corolla_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Corolla&modelYear=2021`
- UTC time: 2026-11-04T12:36:00Z | HTTP Date: Wed, 04 Nov 2026 12:36:03 GMT | Count: 1 | bytes: 1491
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"23V865000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"20/12/2023","Component":"AIR BAGS:SENSOR:OCCUPANT CLASSIFICATION","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2020-2021 Avalon, Avalon Hybrid, Corolla, Highlander, Highlander Hybrid, RAV4, RAV4 Hybrid, Lexus ES350, Lexus RX350, Lexus RX450H, 2021 Sienna Hybrid, Lexus ES250, 2020-2022 Camry, Camry Hybrid, and ES300H vehicles.  A short circuit may develop in the Occupant Classification System (OCS) sensor, preventing the front passenger air bag from deploying.","Consequence":"An air bag that does not deploy during a crash increases the risk of injury.","Remedy":"Dealers will inspect and replace the sensor as necessary, free of charge.  Interim letters notifying owners of the safety risk were mailed in February 2024.
```
### complaints_Toyota_Corolla_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Corolla&modelYear=2021`
- UTC time: 2026-11-04T12:36:02Z | HTTP Date: Wed, 04 Nov 2026 12:36:06 GMT | Count: 188 | bytes: 181704
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":188,"message":"Results returned successfully","results":[{"odiNumber":11772907,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"05/01/2024","dateComplaintFiled":"10/22/2026","vin":"5YFS4MCE7MP","components":"WHEELS,UNKNOWN OR OTHER","summary":"Front wheel bearings   my vehicle has 63,000 my front right wheel bearing changed at 32,000 - now I need both front wheel bearing replaced","products":[{"type":"Vehicle","productYear":"2021","productMake":"TOYOTA","productModel":"COROLLA","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11772448,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"05/22/2026","dateComplaintFiled":"10/20/2026","vin":"5yfepmae1mp","components":"AIR BAGS","summary":"On May 22, 2026, I got off work and started my 2021 Toyota Corolla LE when I noticed the SRS airbag warning light was on. The warning l
```
### recalls_Toyota_Corolla_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Corolla&modelYear=2022`
- UTC time: 2026-11-04T12:36:06Z | HTTP Date: Wed, 04 Nov 2026 12:36:08 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":0,"Message":"Results returned successfully","results":[]}
```
### complaints_Toyota_Corolla_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Corolla&modelYear=2022`
- UTC time: 2026-11-04T12:36:07Z | HTTP Date: Wed, 04 Nov 2026 12:36:11 GMT | Count: 102 | bytes: 102723
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":102,"message":"Results returned successfully","results":[{"odiNumber":11771638,"manufacturer":"Toyota Motor Corporation","crash":true,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/16/2026","dateComplaintFiled":"10/16/2026","vin":"JTDS4MCE9N3","components":"VEHICLE SPEED CONTROL,UNKNOWN OR OTHER","summary":"Was backing up trying to park vehicle and suddenly vehicle accelerated forward on his own causing an accident (hit a pole).  Smoke started coming out of the hood.","products":[{"type":"Vehicle","productYear":"2022","productMake":"TOYOTA","productModel":"COROLLA","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11767802,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/28/2026","dateComplaintFiled":"09/29/2026","vin":"5YFS4MCE9NP","components":"FUEL/PROPULSION SYSTEM","summary":"I currently am experiencing the early stages of the failure of the SECOND fuel pump
```
### recalls_Toyota_Corolla_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Corolla&modelYear=2023`
- UTC time: 2026-11-04T12:36:10Z | HTTP Date: Wed, 04 Nov 2026 12:36:13 GMT | Count: 3 | bytes: 4167
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"23V480000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"12/07/2023","Component":"STEERING:COLUMN","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2023 Corolla, Corolla Cross, Corolla Cross Hybrid, Highlander, Highlander Hybrid, Tacoma, 2023 Lexus RX350, RX350 Hybrid, RX500 Hybrid, 2023-2024 Lexus NX250, NX350, and NX350 Hybrid vehicles.  An electrical connection inside the steering column's spiral cable assembly may be insufficiently welded, causing the connection to separate and deactivate the driver's air bag.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 208, \"Occupant Crash Protection.\"","Consequence":"A deactivated driver's air bag that does not deploy as intended increases the risk of injury during a c
```
### complaints_Toyota_Corolla_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Corolla&modelYear=2023`
- UTC time: 2026-11-04T12:36:13Z | HTTP Date: Wed, 04 Nov 2026 12:36:16 GMT | Count: 74 | bytes: 80877
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":74,"message":"Results returned successfully","results":[{"odiNumber":11771374,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":true,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"05/14/2026","dateComplaintFiled":"10/15/2026","vin":"JTND4MBE9P3","components":"ELECTRICAL SYSTEM","summary":"The contact owns a 2023 Toyota Corolla. The contact stated that while the vehicle was unoccupied and parked in the driveway, the vehicle caught fire. The fire originated from the engine bayapproximately five minutes after the vehicle was started. The fire department extinguished the flames and determined that the source of the fire was the battery. Both the manufacturer and the dealer were notified of the failure. The failure mileage was 80,000.","products":[{"type":"Vehicle","productYear":"2023","productMake":"TOYOTA","productModel":"COROLLA","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11762380,"manufacturer":"Toyota Motor Corporation","crash":false,"fir
```
### probe_Jeep_Grand_Cherokee_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2021`
- UTC time: 2026-11-04T12:36:15Z | HTTP Date: Wed, 04 Nov 2026 12:36:19 GMT | Count: 411 | bytes: 427961
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":411,"message":"Results returned successfully","results":[{"odiNumber":11774531,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"07/28/2026","dateComplaintFiled":"10/29/2026","vin":"1C4RJFCG6MC","components":"POWER TRAIN","summary":"The contact owns a 2021 Jeep Grand Cherokee. The contact stated that while driving 70 MPH, the accelerator pedal was depressed; however, the vehicle failed to accelerate as intended and the vehicle jerked abnormally. The vehicle was taken to the dealer; however, the failure was not duplicated. The failure was a persistent failure. The vehicle was taken to an independent mechanic where it was diagnosed with transmission failure. The contact was informed that there were metal shavings inside the oil pan. The contact was informed that the transmission needed to be replaced. The vehicle was being repaired. The manufacturer was contacted and made aware of the failure. The failure
```
### recalls_Jeep_Grand_Cherokee_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2021`
- UTC time: 2026-11-04T12:36:19Z | HTTP Date: Wed, 04 Nov 2026 12:36:21 GMT | Count: 12 | bytes: 14390
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":12,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"21V797000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"14/10/2021","Component":"EXTERIOR LIGHTING:HEADLIGHTS","Summary":"Chrysler (FCA US, LLC) is recalling certain 2021 Jeep Grand Cherokee L vehicles not equipped with automatic high beams.  When the master lighting switch is set to the auto position, the high beam headlights will not activate unless the master lighting switch is first changed to the 'on\" position.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 108, \"Lamps, Reflective Devices, and Associated Equipment.\"","Consequence":"Difficulty activating the headlight high beams may result in reduced visibility, increasing the risk of a crash.","Remedy":"Dealers will reprogram the vehicles, free of charge.  Owner notification letters were mailed October 
```
### complaints_Jeep_Grand_Cherokee_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2021`
- UTC time: 2026-11-04T12:36:20Z | HTTP Date: Wed, 04 Nov 2026 12:36:24 GMT | Count: 411 | bytes: 427961
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":411,"message":"Results returned successfully","results":[{"odiNumber":11774531,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"07/28/2026","dateComplaintFiled":"10/29/2026","vin":"1C4RJFCG6MC","components":"POWER TRAIN","summary":"The contact owns a 2021 Jeep Grand Cherokee. The contact stated that while driving 70 MPH, the accelerator pedal was depressed; however, the vehicle failed to accelerate as intended and the vehicle jerked abnormally. The vehicle was taken to the dealer; however, the failure was not duplicated. The failure was a persistent failure. The vehicle was taken to an independent mechanic where it was diagnosed with transmission failure. The contact was informed that there were metal shavings inside the oil pan. The contact was informed that the transmission needed to be replaced. The vehicle was being repaired. The manufacturer was contacted and made aware of the failure. The failure
```
### recalls_Jeep_Grand_Cherokee_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2022`
- UTC time: 2026-11-04T12:36:24Z | HTTP Date: Wed, 04 Nov 2026 12:36:27 GMT | Count: 13 | bytes: 16107
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":13,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"23V577000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"14/08/2023","Component":"BACK OVER PREVENTION:DISPLAY FUNCTION","Summary":"Chrysler (FCA US, LLC) is recalling certain 2022-2023 Jeep Grand Cherokee, 2021-2023 Jeep Grand Cherokee L, and 2022-2024 Jeep Wagoneer and Grand Wagoneer vehicles.  The Central Vision Park Assist module (CVPAM) software may prevent the rearview image from displaying when the vehicle is placed in reverse.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 111, \"Rear Visibility.\"","Consequence":"A rearview image that does not display while in reverse decreases the driver's visibility of the rear view, increasing the risk of injury or crash.","Remedy":"Dealers will update the Central Vision Park Assist Module software, free of charge.  
```
### complaints_Jeep_Grand_Cherokee_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2022`
- UTC time: 2026-11-04T12:36:26Z | HTTP Date: Wed, 04 Nov 2026 12:36:30 GMT | Count: 379 | bytes: 445771
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":379,"message":"Results returned successfully","results":[{"odiNumber":11774808,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/27/2026","dateComplaintFiled":"10/31/2026","vin":"1C4RJYE66N8","components":"POWER TRAIN,ENGINE,FUEL/PROPULSION SYSTEM","summary":"Hybrid engine failure. Jeep vehicle is unsafe to drive as the electric engine doesn’t work due to overheating and charging error codes, which causes power to jump between electric and gas engine spontaneously causing speed control to be unpredictable and unsafe.   There is also the question that there is a serious defect with the battery and unsafe to park this vehicle in a garage attached to a dwelling unit.","products":[{"type":"Vehicle","productYear":"2022","productMake":"JEEP","productModel":"GRAND CHEROKEE","manufacturer":"Chrysler (FCA US, LLC)"}]},{"odiNumber":11774580,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"
```
### recalls_Jeep_Grand_Cherokee_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2023`
- UTC time: 2026-11-04T12:36:30Z | HTTP Date: Wed, 04 Nov 2026 12:36:34 GMT | Count: 21 | bytes: 25626
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":21,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"23V336000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"11/05/2023","Component":"EQUIPMENT:OTHER:LABELS","Summary":"Chrysler (FCA US, LLC) is recalling certain 2022-2023 Jeep Grand Cherokee L and Grand Cherokee vehicles.  The air bag warning label may be missing from the dashboard.  As such, these vehicles fail to comply with the requirement Federal Motor Vehicle Safety Standard number 208, \"Occupant Crash Protection.\"","Consequence":"Without a label that shows the proper restraint usage guidelines, the occupants may have an increased risk of injury in the event of a crash.","Remedy":"FCA US, LLC will mail owners the warning label information, free of charge.  Dealers will inspect unsold vehicles and install the required label, as necessary, free of charge.  Owner notification letters were mailed May 25, 2023.  Owners ma
```
### complaints_Jeep_Grand_Cherokee_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Grand%20Cherokee&modelYear=2023`
- UTC time: 2026-11-04T12:36:33Z | HTTP Date: Wed, 04 Nov 2026 12:36:37 GMT | Count: 408 | bytes: 467318
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":408,"message":"Results returned successfully","results":[{"odiNumber":11774326,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/28/2026","dateComplaintFiled":"10/28/2026","vin":"1C4RJYC65P8","components":"FUEL/PROPULSION SYSTEM","summary":"After receiving the 68C update my vehicle has had a constant power drain from the high voltage battery that lessens the advertised mileage in all electric mode. In addition, the power output in all electric mode is severely reduced and poses a safety issue when attempting to merge into traffic or when having to accelerate to avoid a hazard.","products":[{"type":"Vehicle","productYear":"2023","productMake":"JEEP","productModel":"GRAND CHEROKEE","manufacturer":"Chrysler (FCA US, LLC)"}]},{"odiNumber":11774116,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/23/2026","dateComplaintFiled":"
```
### probe_Ford_Edge_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Edge&modelYear=2021`
- UTC time: 2026-11-04T12:36:37Z | HTTP Date: Wed, 04 Nov 2026 12:36:40 GMT | Count: 114 | bytes: 102077
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":114,"message":"Results returned successfully","results":[{"odiNumber":11772380,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/20/2026","dateComplaintFiled":"10/20/2026","vin":"2FMPK4K94MB","components":"POWER TRAIN","summary":"The transmission jerks VERY strongly when shifting gears between 5mph - 60mpg. It is so pronounced that it effects my foot on the pedals and could cause drivers to slam on the accelerator or brake. The vehicle has 90k miles on it and this issue has been happening for 10k miles or so.   This is a KNOWN issue with the 8F35 transmission and needs to be a recall instead of a TSB that costs drivers $5k.","products":[{"type":"Vehicle","productYear":"2021","productMake":"FORD","productModel":"EDGE","manufacturer":"Ford Motor Company"}]},{"odiNumber":11772261,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"07/15/20
```
### recalls_Ford_Edge_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Edge&modelYear=2021`
- UTC time: 2026-11-04T12:36:39Z | HTTP Date: Wed, 04 Nov 2026 12:36:42 GMT | Count: 7 | bytes: 8449
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":7,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"21V011000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"15/01/2021","Component":"POWER TRAIN:DRIVELINE:DRIVESHAFT","Summary":"Ford Motor Company (Ford) is recalling certain 2020-2021 Edge, 2020 Lincoln Nautilus and Ford Escape and 2021 Lincoln Corsair and Ford Bronco Sport vehicles.  An inadequate amount of lubricant in the rear drive unit may cause seizure of the rear drive axle.","Consequence":"If the rear drive unit seizes, there may be a loss of drive and/or a loss of vehicle control, increasing the risk of a crash.","Remedy":"Ford will notify owners, and dealers will check the rear drive unit lubricant level.  Axles found to have lubricant at the minimum level will be filled to the full level.  Axles found to be below the minimum lubricant fill level will be replaced, free of charge.  This recall began March 12, 2021.  Own
```
### complaints_Ford_Edge_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Edge&modelYear=2021`
- UTC time: 2026-11-04T12:36:41Z | HTTP Date: Wed, 04 Nov 2026 12:36:43 GMT | Count: 114 | bytes: 102077
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":114,"message":"Results returned successfully","results":[{"odiNumber":11772380,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/20/2026","dateComplaintFiled":"10/20/2026","vin":"2FMPK4K94MB","components":"POWER TRAIN","summary":"The transmission jerks VERY strongly when shifting gears between 5mph - 60mpg. It is so pronounced that it effects my foot on the pedals and could cause drivers to slam on the accelerator or brake. The vehicle has 90k miles on it and this issue has been happening for 10k miles or so.   This is a KNOWN issue with the 8F35 transmission and needs to be a recall instead of a TSB that costs drivers $5k.","products":[{"type":"Vehicle","productYear":"2021","productMake":"FORD","productModel":"EDGE","manufacturer":"Ford Motor Company"}]},{"odiNumber":11772261,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"07/15/20
```
### recalls_Ford_Edge_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Edge&modelYear=2022`
- UTC time: 2026-11-04T12:36:43Z | HTTP Date: Wed, 04 Nov 2026 12:36:45 GMT | Count: 5 | bytes: 6030
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":5,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"22V151000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":true,"ReportReceivedDate":"12/03/2022","Component":"BACK OVER PREVENTION:DISPLAY FUNCTION","Summary":"Ford Motor Company (Ford) is recalling certain 2021-2022 Edge vehicles.  A software error may cause the rearview camera to display a blank or distorted image when the vehicle is in reverse.","Consequence":"A rearview camera that displays a blank or distorted image can reduce the driver's view of what is behind the vehicle, increasing the risk of a crash.","Remedy":"The rearview camera software will be updated by a dealer, or through an over-the-air (OTA) update, free of charge.  Owner notification letters were mailed on April 29, 2022.  Owners may contact Ford customer service at 1-866-436-7332.  Ford's number for this recall is 22S14.","Notes":"Owners may also contact the National Highway Traffic Sa
```
### complaints_Ford_Edge_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Edge&modelYear=2022`
- UTC time: 2026-11-04T12:36:45Z | HTTP Date: Wed, 04 Nov 2026 12:36:48 GMT | Count: 135 | bytes: 130908
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":135,"message":"Results returned successfully","results":[{"odiNumber":11774879,"manufacturer":"Ford Motor Company","crash":true,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/16/2026","dateComplaintFiled":"10/31/2026","vin":"2FMPK4G97NB","components":"AIR BAGS","summary":"Hit a deer on the highway at speeds around 60mph, car was totaled, no air bags deployed.","products":[{"type":"Vehicle","productYear":"2022","productMake":"FORD","productModel":"EDGE","manufacturer":"Ford Motor Company"}]},{"odiNumber":11773676,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"06/01/2026","dateComplaintFiled":"10/26/2026","vin":"2FMPK4K93NB","components":"POWER TRAIN","summary":"The contact owns a 2022 Ford Edge. The contact stated that while driving approximately 30 - 40 MPH, the transmission unexpectedly failed to operate as needed. The contact stated that due to the failure, the vehicle unexpe
```
### recalls_Ford_Edge_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Edge&modelYear=2023`
- UTC time: 2026-11-04T12:36:48Z | HTTP Date: Wed, 04 Nov 2026 12:36:51 GMT | Count: 4 | bytes: 5078
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"23V198000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"24/03/2023","Component":"CHILD SEAT:VEHICLE TETHER ANCHOR","Summary":"Ford Motor Company (Ford) is recalling certain 2023 Edge and Lincoln Nautilus vehicles.  The child seat tether wire welds on the second-row left-side seat back frame may be insufficient, which can reduce the seat's ability to properly restrain a child during a crash.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 225, \"Child Restraint Anchorage Systems.\"","Consequence":"A child that is not properly restrained during a crash can have an increased risk of injury.","Remedy":"Dealers will replace the left-side second-row seat back frame, free of charge.  Owner notification letters were mailed May 11, 2023.  Owners may contact Ford customer serv
```
### complaints_Ford_Edge_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Edge&modelYear=2023`
- UTC time: 2026-11-04T12:36:51Z | HTTP Date: Wed, 04 Nov 2026 12:36:55 GMT | Count: 23 | bytes: 22172
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":23,"message":"Results returned successfully","results":[{"odiNumber":11768884,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/25/2026","dateComplaintFiled":"10/04/2026","vin":"2FMPK4J93PB","components":"Other/I am not sure","summary":"The ClickTight mechanism is what allows the car seat to be moved in/out of the vehicle after securing using the seatbelt of the vehicle. Essentially, this mechanism causes the bottom of the car seat to fold up and allows the parent to unlatch the seatbelt to move the car seat. This mechanism is spring loaded and is supposed to lock/unlock by simply squeezing together two red handles. On my car seat, this mechanism has become stuck and does not allow the mechanism to lock into place & secure the car seat onto the seat belt. I am unsure of what is causing this jam, but I have only purchased this car seat on May 15, 2026 in brand new condition from Amazon. I have not been in
```
### probe_Subaru_Forester_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Forester&modelYear=2021`
- UTC time: 2026-11-04T12:36:59Z | HTTP Date: Wed, 04 Nov 2026 12:37:03 GMT | Count: 215 | bytes: 223436
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":215,"message":"Results returned successfully","results":[{"odiNumber":11774980,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/11/2026","dateComplaintFiled":"11/01/2026","vin":"JF2SKASC9MH","components":"POWER TRAIN,ELECTRICAL SYSTEM,ENGINE","summary":"When coming to a stop, the auto start/stop system shuts the engine off and it fails to restart. All dashboard warning lights illuminate. The vehicle must be shifted to Park and restarted manually with the start button. The component that failed is the auto start/stop system; the exact cause is UNKNOWN. The vehicle is available for inspection upon request. This put safety at risk because the vehicle was left immobile in live traffic at stops until it could be restarted. There were no warning lamps or symptoms before the failure; the warning lights come on when the failure occurs. The vehicle was inspected by Gillman Subaru Southwest on October 229, 2
```
### recalls_Subaru_Forester_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Forester&modelYear=2021`
- UTC time: 2026-11-04T12:37:03Z | HTTP Date: Wed, 04 Nov 2026 12:37:06 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":0,"Message":"Results returned successfully","results":[]}
```
### complaints_Subaru_Forester_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Forester&modelYear=2021`
- UTC time: 2026-11-04T12:37:05Z | HTTP Date: Wed, 04 Nov 2026 12:37:08 GMT | Count: 215 | bytes: 223436
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":215,"message":"Results returned successfully","results":[{"odiNumber":11774980,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/11/2026","dateComplaintFiled":"11/01/2026","vin":"JF2SKASC9MH","components":"POWER TRAIN,ELECTRICAL SYSTEM,ENGINE","summary":"When coming to a stop, the auto start/stop system shuts the engine off and it fails to restart. All dashboard warning lights illuminate. The vehicle must be shifted to Park and restarted manually with the start button. The component that failed is the auto start/stop system; the exact cause is UNKNOWN. The vehicle is available for inspection upon request. This put safety at risk because the vehicle was left immobile in live traffic at stops until it could be restarted. There were no warning lamps or symptoms before the failure; the warning lights come on when the failure occurs. The vehicle was inspected by Gillman Subaru Southwest on October 229, 2
```
### recalls_Subaru_Forester_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Forester&modelYear=2022`
- UTC time: 2026-11-04T12:37:07Z | HTTP Date: Wed, 04 Nov 2026 12:37:10 GMT | Count: 1 | bytes: 1188
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Subaru of America, Inc.","NHTSACampaignNumber":"23V755000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"09/11/2023","Component":"POWER TRAIN:AUTOMATIC TRANSMISSION:PARK/NEUTRAL START INTERLOCK SWITCH","Summary":"Subaru of America, Inc. is recalling certain model year 2021 Crosstrek, 2022 Forester, 2021-2023 Legacy, and Outback vehicles.  An insufficient weld may allow water to enter the inhibitor switch, causing it to fail.","Consequence":"An inoperative inhibitor switch may prevent the reverse lights from illuminating and the rearview camera image from displaying, increasing the risk of a crash.","Remedy":"Dealers will replace the inhibitor switch, free of charge.  Owner notification letters were mailed January 8, 2024.  Owners may contact Subaru customer service at 1-800-782-2783.  Subaru's number for this recall is WRQ-23.","Notes":"Owners may also contact the Nation
```
### complaints_Subaru_Forester_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Forester&modelYear=2022`
- UTC time: 2026-11-04T12:37:09Z | HTTP Date: Wed, 04 Nov 2026 12:37:12 GMT | Count: 100 | bytes: 106340
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":100,"message":"Results returned successfully","results":[{"odiNumber":11772203,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/12/2026","dateComplaintFiled":"10/19/2026","vin":"JF2SKAMC3NH","components":"ENGINE","summary":"Head gasket failure. Caused oil in coolant. Caused coolant hose to break while driving. Subaru dealership says need to replace head gaskets, radiator, all hoses, cvt cooler(?), and will cost about $6400.  My car has about 130000 miles.  This seems to be rather unusual at this mileage.","products":[{"type":"Vehicle","productYear":"2022","productMake":"SUBARU","productModel":"FORESTER","manufacturer":"Subaru of America, Inc."}]},{"odiNumber":11771742,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/11/2026","dateComplaintFiled":"10/16/2026","vin":"JF2SKAPC5NH","components":"ELECTRICAL SYSTEM,SERVICE BR
```
### recalls_Subaru_Forester_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Forester&modelYear=2023`
- UTC time: 2026-11-04T12:37:12Z | HTTP Date: Wed, 04 Nov 2026 12:37:14 GMT | Count: 1 | bytes: 1221
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Subaru of America, Inc.","NHTSACampaignNumber":"23V754000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"09/11/2023","Component":"POWER TRAIN:DRIVELINE:DRIVESHAFT","Summary":"Subaru of America, Inc. (Subaru) is recalling certain 2024 Crosstrek, Impreza, 2023-2024 Forester, and 2023 WRX vehicles.  The front driveshaft assemblies' outer race may develop cracks and break.","Consequence":"A broken driveshaft can cause a loss of drive power while driving or vehicle rollaway when the vehicle is in park without the parking brake engaged.  Either of these scenarios can increase the risk of a crash.","Remedy":"Dealers will inspect and replace the left and right front driveshafts as necessary, free of charge.  Owner notification letters were mailed January 8, 2024.  Owners may contact Subaru's customer service at 1-844-373-6614.  Subaru's number for this recall is WRP-23.","Notes"
```
### complaints_Subaru_Forester_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Forester&modelYear=2023`
- UTC time: 2026-11-04T12:37:13Z | HTTP Date: Wed, 04 Nov 2026 12:37:16 GMT | Count: 74 | bytes: 81936
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":74,"message":"Results returned successfully","results":[{"odiNumber":11768438,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":1,"numberOfDeaths":0,"dateOfIncident":"08/24/2026","dateComplaintFiled":"10/02/2026","vin":"Jf2skamc9ph","components":"POWER TRAIN,ELECTRICAL SYSTEM,SERVICE BRAKES","summary":"Transmission slipped, stranded me in the middle of a road XXX. Stopped wouldn’t go.  Started locking down in reverse 1 month after I purchased the vehicle. XXX, my husband was backing down a road that had no turnaround. The RAB locked down, slammed so hard, the car slid six feet and the motor shut down. I found out a week later that L-5 was fractured in my back. The lockdown has hurt my [XXX] mother’s neck also, in March of this year. The friction clutches is fried in my transmission. My transmission is jerking, slipping, clanking, shaking from multiple lockdowns. I took vehicle to [XXX] Subaru XXX for service. I told [XXX] about  it lock
```
### probe_Jeep_Wrangler_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Wrangler&modelYear=2021`
- UTC time: 2026-11-04T12:37:16Z | HTTP Date: Wed, 04 Nov 2026 12:37:20 GMT | Count: 960 | bytes: 1044381
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":960,"message":"Results returned successfully","results":[{"odiNumber":11775100,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/10/2026","dateComplaintFiled":"11/02/2026","vin":"1C4JJXP68MW","components":"ELECTRICAL SYSTEM","summary":"The vehicle has lost power multiple times and have been at the dealership now twice due to it first time the check engine light went off before the dealership could find an issue and they couldn’t find anything second time after losing power on the expressway. They check engine light came on for a few days and went off by time my appointment at the dealership. The determined the PIM had issues and are replacing it.","products":[{"type":"Vehicle","productYear":"2021","productMake":"JEEP","productModel":"WRANGLER","manufacturer":"Chrysler (FCA US, LLC)"}]},{"odiNumber":11774999,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":true,"numberOfInjuries":0,"numb
```
### recalls_Jeep_Wrangler_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Wrangler&modelYear=2021`
- UTC time: 2026-11-04T12:37:20Z | HTTP Date: Wed, 04 Nov 2026 12:37:23 GMT | Count: 15 | bytes: 18208
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":15,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"21V028000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"28/01/2021","Component":"POWER TRAIN:CLUTCH ASSEMBLY","Summary":"Chrysler (FCA US, LLC) is recalling certain 2018-2021 Jeep Wrangler and 2020-2021 Jeep Gladiator vehicles equipped with manual transmissions.  The clutch pressure plate may overheat and fracture.","Consequence":"Overheated clutch components may increase the risk of a fire.  Additionally, damage to other nearby components can result in debris falling onto the road or a loss of drive, increasing the risk of a crash.","Remedy":"FCA US LLC will notify owners, and dealers will add software to reduce engine torque capability when clutch assembly temperatures rise to a level that may damage the inner pressure plate, free of charge.\"  FCA has ordered a stop sale for the affected vehicles as of February 25, 2021
```
### complaints_Jeep_Wrangler_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Wrangler&modelYear=2021`
- UTC time: 2026-11-04T12:37:22Z | HTTP Date: Wed, 04 Nov 2026 12:37:27 GMT | Count: 960 | bytes: 1044381
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":960,"message":"Results returned successfully","results":[{"odiNumber":11775100,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/10/2026","dateComplaintFiled":"11/02/2026","vin":"1C4JJXP68MW","components":"ELECTRICAL SYSTEM","summary":"The vehicle has lost power multiple times and have been at the dealership now twice due to it first time the check engine light went off before the dealership could find an issue and they couldn’t find anything second time after losing power on the expressway. They check engine light came on for a few days and went off by time my appointment at the dealership. The determined the PIM had issues and are replacing it.","products":[{"type":"Vehicle","productYear":"2021","productMake":"JEEP","productModel":"WRANGLER","manufacturer":"Chrysler (FCA US, LLC)"}]},{"odiNumber":11774999,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":true,"numberOfInjuries":0,"numb
```
### recalls_Jeep_Wrangler_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Wrangler&modelYear=2022`
- UTC time: 2026-11-04T12:37:27Z | HTTP Date: Wed, 04 Nov 2026 12:37:30 GMT | Count: 15 | bytes: 18666
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":15,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"22V326000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"12/05/2022","Component":"EXTERIOR LIGHTING","Summary":"Chryler (FCA US, LLC) is recalling certain 2022 Jeep Wrangler vehicles.  The side marker lights may not function due to an incompatible tail light assembly wiring harness.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 108, \"Lamps, Reflective Devices, and Associated Equipment.\"","Consequence":"Nonfunctional side marker lights may reduce vehicle visibility to other drivers, increasing the risk of a crash.","Remedy":"FCA will replace the tail light assemblies, free of charge.  Owner notification letters were mailed on May 26, 2022 and August 3, 2023.  Owners may contact FCA US, LLC customer service at 1-800-853-1403.  FCA US, LLC's number for this reca
```
### complaints_Jeep_Wrangler_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Wrangler&modelYear=2022`
- UTC time: 2026-11-04T12:37:30Z | HTTP Date: Wed, 04 Nov 2026 12:37:33 GMT | Count: 413 | bytes: 479834
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":413,"message":"Results returned successfully","results":[{"odiNumber":11774893,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/26/2026","dateComplaintFiled":"10/31/2026","vin":"1c4jjxsj4nw","components":"STEERING","summary":"While driving above 50 mph,  if you hit a bump the steering wheel shakes violently and it's hard to control the Jeep.","products":[{"type":"Vehicle","productYear":"2022","productMake":"JEEP","productModel":"WRANGLER","manufacturer":"Chrysler (FCA US, LLC)"}]},{"odiNumber":11774465,"manufacturer":"Chrysler (FCA US, LLC)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/01/2026","dateComplaintFiled":"10/29/2026","vin":"1C4JJXP60NW","components":"STEERING,SUSPENSION","summary":"My vehicle experiences violent front end steering and suspension oscillation ('death wobble') at highway speeds approaching 70 mph, I hit any road bump and it is trigg
```
### recalls_Jeep_Wrangler_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Jeep&model=Wrangler&modelYear=2023`
- UTC time: 2026-11-04T12:37:33Z | HTTP Date: Wed, 04 Nov 2026 12:37:36 GMT | Count: 14 | bytes: 18202
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":14,"Message":"Results returned successfully","results":[{"Manufacturer":"Chrysler (FCA US, LLC)","NHTSACampaignNumber":"22V768000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"13/10/2022","Component":"ELECTRICAL SYSTEM:PROPULSION SYSTEM:TRACTION BATTERY","Summary":"Chrysler (FCA US, LLC) is recalling certain 2022-2023 Jeep Wrangler Plug-In Hybrid Electric (PHEV) vehicles.  The high voltage (HV) battery pack assembly was built with incorrect fasteners to secure the 200-amp fuse, which can generate excessive heat.","Consequence":"Excessive heat may cause the fuse to fail and result in a loss of drive power, increasing the risk of a crash.","Remedy":"Dealers will inspect and replace the HV battery fuse, as necessary.  Dealers will also inspect the battery assembly for damage and replace it, if necessary.  Repairs will be performed free of charge.  Owner notification letters were mailed December 8, 2022.  Owners may contact Chrysler customer se
```
### complaints_Jeep_Wrangler_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Jeep&model=Wrangler&modelYear=2023`
- UTC time: 2026-11-04T12:37:35Z | HTTP Date: Wed, 04 Nov 2026 12:37:39 GMT | Count: 376 | bytes: 447775
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":376,"message":"Results returned successfully","results":[{"odiNumber":11774883,"manufacturer":"Chrysler (FCA US, LLC)","crash":true,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"07/09/2026","dateComplaintFiled":"10/31/2026","vin":"1C4JJXP62PW","components":"ELECTRICAL SYSTEM,FUEL/PROPULSION SYSTEM","summary":"I am reporting repeated safety-related failures involving my 2023 Jeep Wrangler 4xe Sahara 4x4, VIN 1C4JJXP62PW524360.  The vehicle has experienced recurring failures involving the high-voltage battery, hybrid charging/propulsion system, electric coolant heater, and battery thermal-management system.  On 7/17/2025, at about 60,291 miles, the vehicle displayed a check-engine light and “Service Charging System” warning. While stopping, the vehicle shut off and would not restart without assistance. A/C stopped working and EV operation was unavailable. The dealer performed FCA 95B high-voltage-battery recall/software work.  The problem returned. F
```
### probe_Toyota_Highlander_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Highlander&modelYear=2021`
- UTC time: 2026-11-04T12:37:39Z | HTTP Date: Wed, 04 Nov 2026 12:37:43 GMT | Count: 535 | bytes: 544206
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":535,"message":"Results returned successfully","results":[{"odiNumber":11774350,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/26/2026","dateComplaintFiled":"10/29/2026","vin":"5TDHZRBH5MS","components":"POWER TRAIN","summary":"My 2021 Toyota Highlander XLE began making a high-pitched whining noise when accelerating. When researching this noise, associated with the make, model, and year of my vehicle, it became apparent that the noise is associated with a manufacturer's defect in the [XXX]‑speed transmission (Toyota [XXX]).  The cited notification states that the correction for this defect is a transmission replacement that is only covered by the 60,000 mile/5 Year warranty.  There are three class-action lawsuits associated with this issue, and I wanted to document my incident in the event that my service appointment with [XXX] Toyota in [XXX], on 11/23/2026 indicates that my transmission is af
```
### recalls_Toyota_Highlander_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Highlander&modelYear=2021`
- UTC time: 2026-11-04T12:37:42Z | HTTP Date: Wed, 04 Nov 2026 12:37:45 GMT | Count: 4 | bytes: 4725
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"23V720000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"26/10/2023","Component":"STRUCTURE:BODY:BUMPERS","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2020-2023 Highlander & Highlander Hybrid vehicles.  During normal vehicle operation, minor impact to the front lower bumper cover may result in the cover coming loose or detaching.","Consequence":"A detached front bumper cover can become a road hazard, increasing the risk of a crash.","Remedy":"Dealers will repair or replace the upper and lower front bumper covers as necessary, free of charge.  Owner letters were mailed April 22, 2024.  Owners may contact Toyota customer service at 1-800-331-4331.  Toyota's number for this recall is 23TB12/23TA12.","Notes":"Owners may also contact the National Highway Traffic Safety Admini
```
### complaints_Toyota_Highlander_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Highlander&modelYear=2021`
- UTC time: 2026-11-04T12:37:44Z | HTTP Date: Wed, 04 Nov 2026 12:37:47 GMT | Count: 535 | bytes: 544206
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":535,"message":"Results returned successfully","results":[{"odiNumber":11774350,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/26/2026","dateComplaintFiled":"10/29/2026","vin":"5TDHZRBH5MS","components":"POWER TRAIN","summary":"My 2021 Toyota Highlander XLE began making a high-pitched whining noise when accelerating. When researching this noise, associated with the make, model, and year of my vehicle, it became apparent that the noise is associated with a manufacturer's defect in the [XXX]‑speed transmission (Toyota [XXX]).  The cited notification states that the correction for this defect is a transmission replacement that is only covered by the 60,000 mile/5 Year warranty.  There are three class-action lawsuits associated with this issue, and I wanted to document my incident in the event that my service appointment with [XXX] Toyota in [XXX], on 11/23/2026 indicates that my transmission is af
```
### recalls_Toyota_Highlander_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Highlander&modelYear=2022`
- UTC time: 2026-11-04T12:37:47Z | HTTP Date: Wed, 04 Nov 2026 12:37:50 GMT | Count: 5 | bytes: 5786
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":5,"Message":"Results returned successfully","results":[{"Manufacturer":"Gulf States Toyota, Inc.","NHTSACampaignNumber":"22V310000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"06/05/2022","Component":"EQUIPMENT:OTHER:LABELS","Summary":"Gulf States Toyota, Inc. (GST) is recalling certain 2022 4Runner, Tacoma, Highlander, and Highlander Hybrid vehicles.  The load carrying capacity modification labels may not be permanent and can fade, becoming illegible.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 110, \"Tire Selection and Rims.\"","Consequence":"An illegible label may allow the vehicle to be overloaded, increasing the risk of a crash.","Remedy":"GST will notify owners by mail, including a replacement load carrying capacity modification label for their vehicle and detailed replacement instructions, free of charge.  Owner notification letters were mailed June 30, 2022.  Owners 
```
### complaints_Toyota_Highlander_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Highlander&modelYear=2022`
- UTC time: 2026-11-04T12:37:49Z | HTTP Date: Wed, 04 Nov 2026 12:37:52 GMT | Count: 266 | bytes: 262469
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":266,"message":"Results returned successfully","results":[{"odiNumber":11773377,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/15/2026","dateComplaintFiled":"10/24/2026","vin":"5TDFARAH7NS","components":"ELECTRICAL SYSTEM,AIR BAGS,FORWARD COLLISION AVOIDANCE","summary":"Headlight system malfunction, pre-collision system malfunction, LTA malfunction, SRS airbag system malfunction and SRS malfunction lights came on after start up.","products":[{"type":"Vehicle","productYear":"2022","productMake":"TOYOTA","productModel":"HIGHLANDER","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11773397,"manufacturer":"Toyota Motor Corporation","crash":true,"fire":false,"numberOfInjuries":1,"numberOfDeaths":0,"dateOfIncident":"10/22/2026","dateComplaintFiled":"10/24/2026","vin":"5TDFZRAH6NS","components":"ELECTRICAL SYSTEM,SERVICE BRAKES,ENGINE","summary":"On October 22, 2026 at 7:55pm I was slowly pulli
```
### recalls_Toyota_Highlander_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Toyota&model=Highlander&modelYear=2023`
- UTC time: 2026-11-04T12:37:52Z | HTTP Date: Wed, 04 Nov 2026 12:37:54 GMT | Count: 9 | bytes: 11719
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":9,"Message":"Results returned successfully","results":[{"Manufacturer":"Toyota Motor Engineering & Manufacturing","NHTSACampaignNumber":"23V480000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"12/07/2023","Component":"STEERING:COLUMN","Summary":"Toyota Motor Engineering & Manufacturing (Toyota) is recalling certain 2023 Corolla, Corolla Cross, Corolla Cross Hybrid, Highlander, Highlander Hybrid, Tacoma, 2023 Lexus RX350, RX350 Hybrid, RX500 Hybrid, 2023-2024 Lexus NX250, NX350, and NX350 Hybrid vehicles.  An electrical connection inside the steering column's spiral cable assembly may be insufficiently welded, causing the connection to separate and deactivate the driver's air bag.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 208, \"Occupant Crash Protection.\"","Consequence":"A deactivated driver's air bag that does not deploy as intended increases the risk of injury during a c
```
### complaints_Toyota_Highlander_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Toyota&model=Highlander&modelYear=2023`
- UTC time: 2026-11-04T12:37:53Z | HTTP Date: Wed, 04 Nov 2026 12:37:56 GMT | Count: 189 | bytes: 186455
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":189,"message":"Results returned successfully","results":[{"odiNumber":11772589,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"03/05/2026","dateComplaintFiled":"10/21/2026","vin":"5TDKDRAH4PS","components":"SEATS","summary":"Recall has not been fixed in a timely manner.","products":[{"type":"Vehicle","productYear":"2023","productMake":"TOYOTA","productModel":"HIGHLANDER","manufacturer":"Toyota Motor Corporation"}]},{"odiNumber":11772322,"manufacturer":"Toyota Motor Corporation","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"03/01/2026","dateComplaintFiled":"10/20/2026","vin":"5TDBBRCH3PS","components":"SERVICE BRAKES","summary":"While depressing the brake pedal to come to a complete stop, the vehicle experienced a sudden loss of braking force, followed by a momentary forward surge/lunge before the friction brakes engaged.","products":[{"type":"Vehicle","productY
```
### probe_Hyundai_Tucson_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Hyundai&model=Tucson&modelYear=2021`
- UTC time: 2026-11-04T12:37:56Z | HTTP Date: Wed, 04 Nov 2026 12:37:59 GMT | Count: 80 | bytes: 86327
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":80,"message":"Results returned successfully","results":[{"odiNumber":11770328,"manufacturer":"Hyundai Motor America","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/05/2026","dateComplaintFiled":"10/10/2026","vin":"km8j33al3mu","components":"ELECTRICAL SYSTEM,EXTERIOR LIGHTING,VEHICLE SPEED CONTROL","summary":"loss of info system loss of all dash lights  when I turn the engine off most of the time I loose  all electrical systems (will not start for at least 15 minutes) if doors lock I can only unlock the drivers door with the auxiliary key. Has tried to shift in to park while driving (one time) Lost all power (engine and steering while crossing a highway (once only)","products":[{"type":"Vehicle","productYear":"2021","productMake":"HYUNDAI","productModel":"TUCSON","manufacturer":"Hyundai Motor America"}]},{"odiNumber":11766298,"manufacturer":"Hyundai Motor America","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateO
```
### recalls_Hyundai_Tucson_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Hyundai&model=Tucson&modelYear=2021`
- UTC time: 2026-11-04T12:37:59Z | HTTP Date: Wed, 04 Nov 2026 12:38:01 GMT | Count: 1 | bytes: 1554
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Hyundai Motor America","NHTSACampaignNumber":"20V543000","parkIt":false,"parkOutSide":true,"overTheAirUpdate":false,"NHTSAActionNumber":"PE19003","ReportReceivedDate":"04/09/2020","Component":"SERVICE BRAKES, HYDRAULIC:ANTILOCK/TRACTION CONTROL/ELECTRONIC LIMITED SLIP:CONTROL UNIT/MODULE","Summary":"Hyundai Motor America (Hyundai) recalled certain 2019-2021 Tucson vehicles on September 4, 2020.  On December 30, 2020, Hyundai expanded the recall population, and added certain 2016-2018 Tucson vehicles.  The Anti-lock Brake Hydraulic Electronic Control Unit (HECU) could corrode internally and cause an electrical short, possibly resulting in an engine compartment fire.","Consequence":"An engine compartment fire can increase the risk of injury or crash.","Remedy":"Hyundai will notify owners, and dealers will replace the HECU fuse.  For 2019-2021 model years, the Electronic Stability Control (ESC) software will 
```
### complaints_Hyundai_Tucson_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Hyundai&model=Tucson&modelYear=2021`
- UTC time: 2026-11-04T12:38:01Z | HTTP Date: Wed, 04 Nov 2026 12:38:04 GMT | Count: 80 | bytes: 86327
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":80,"message":"Results returned successfully","results":[{"odiNumber":11770328,"manufacturer":"Hyundai Motor America","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/05/2026","dateComplaintFiled":"10/10/2026","vin":"km8j33al3mu","components":"ELECTRICAL SYSTEM,EXTERIOR LIGHTING,VEHICLE SPEED CONTROL","summary":"loss of info system loss of all dash lights  when I turn the engine off most of the time I loose  all electrical systems (will not start for at least 15 minutes) if doors lock I can only unlock the drivers door with the auxiliary key. Has tried to shift in to park while driving (one time) Lost all power (engine and steering while crossing a highway (once only)","products":[{"type":"Vehicle","productYear":"2021","productMake":"HYUNDAI","productModel":"TUCSON","manufacturer":"Hyundai Motor America"}]},{"odiNumber":11766298,"manufacturer":"Hyundai Motor America","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateO
```
### recalls_Hyundai_Tucson_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Hyundai&model=Tucson&modelYear=2022`
- UTC time: 2026-11-04T12:38:03Z | HTTP Date: Wed, 04 Nov 2026 12:38:06 GMT | Count: 3 | bytes: 3356
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"Hyundai Motor America","NHTSACampaignNumber":"21V938000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"02/12/2021","Component":"ELECTRICAL SYSTEM:SOFTWARE","Summary":"Hyundai Motor America (Hyundai) is recalling certain 2022 Tucson vehicles.  The software installed in the Integrated Central Control Unit (ICU) may be incompatible with the vehicle, which could result in inoperative headlights and/or taillights.","Consequence":"Inoperative headlights or taillights can decrease visibility for both the driver and surrounding traffic, increasing the risk of a crash.","Remedy":"Dealers updated the ICU software, free of charge.  All affected vehicles have been repaired and therefore no owner notification letters will be mailed.  Owners may contact Hyundai customer service at 1-855-371-9460.  Hyundai's number for this recall is 214.","Notes":"Owners may also contact the National 
```
### complaints_Hyundai_Tucson_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Hyundai&model=Tucson&modelYear=2022`
- UTC time: 2026-11-04T12:38:05Z | HTTP Date: Wed, 04 Nov 2026 12:38:09 GMT | Count: 390 | bytes: 438785
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":390,"message":"Results returned successfully","results":[{"odiNumber":11775294,"manufacturer":"Hyundai Motor America","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/28/2026","dateComplaintFiled":"11/02/2026","vin":"KM8JECA11NU","components":"ENGINE","summary":"My wife was driving her 2022 Hyundai Tucson Hybrid, when she suddenly heard a bang and then the vehicle had very little engine power and would not accelerate properly.  This turned out to be because the gas engine would not turn on and only the small hybrid motor was functioning.  She was able to safely pull into a parking lot.   The vehicle was tow to a Hyundai dealership where they diagnosed the issue as a broken/snapped Hybrid Starter Generator (HSG) drive belt tensioner spring. Because this spring failed, the accessory drive belt lost complete tension, and so the HSG could not start the gas engine.  This made the vehicle unsafe to drive due to sever lack of power. The dealersh
```
### recalls_Hyundai_Tucson_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Hyundai&model=Tucson&modelYear=2023`
- UTC time: 2026-11-04T12:38:09Z | HTTP Date: Wed, 04 Nov 2026 12:38:11 GMT | Count: 2 | bytes: 2524
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":2,"Message":"Results returned successfully","results":[{"Manufacturer":"Hyundai Motor America","NHTSACampaignNumber":"23V526000","parkIt":false,"parkOutSide":true,"overTheAirUpdate":false,"ReportReceivedDate":"27/07/2023","Component":"POWER TRAIN:AUTOMATIC TRANSMISSION:FLUID/LUBRICANT:PUMP","Summary":"Hyundai Motor America (Hyundai) is recalling certain 2023-2024 Palisade Tucson, 2023 Sonata, Elantra, and Kona vehicles.  The electronic controller for the Idle Stop & Go oil pump assembly may contain damaged electrical components that can cause the pump controller to overheat.","Consequence":"An electric oil pump assembly that overheats increases the risk of a vehicle fire.","Remedy":"Owners are advised to park outside and away from structures until the recall repair is complete.  Dealers will inspect and replace the electric oil pump controller, as necessary, free of charge.  Owner notification letters were mailed starting September 7, 2023.  Owners may contact Hyundai customer
```
### complaints_Hyundai_Tucson_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Hyundai&model=Tucson&modelYear=2023`
- UTC time: 2026-11-04T12:38:11Z | HTTP Date: Wed, 04 Nov 2026 12:38:15 GMT | Count: 136 | bytes: 154007
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":136,"message":"Results returned successfully","results":[{"odiNumber":11773289,"manufacturer":"Hyundai Motor America","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/10/2026","dateComplaintFiled":"10/23/2026","vin":"5NMJFCAE4PH","components":"STEERING,ELECTRICAL SYSTEM,STRUCTURE","summary":"SAFETY DEFECT SUPPLEMENT TO NHTSA COMPLAINT #11685540 | VIN: [XXX] | MILEAGE: 27,370 ​This filing supplements Complaint #XXX regarding an uncorrected, compounded steering safety failure following the catastrophic detachment of the steering column while driving on XXX (Repair Order #XXX). ​COMPONENTS FAILED: Steering column assembly, footwell closeout shield, dashboard lower crash pad structural frame, and push-start switch. All components and vehicle are available for immediate inspection. ​SAFETY RISK: Following an invasive warranty teardown for an ignition switch failure under R/O #XXX at [XXX] Hyundai, the vehicle was released in an incomplet
```
### probe_Chevrolet_Tahoe_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2021`
- UTC time: 2026-11-04T12:38:15Z | HTTP Date: Wed, 04 Nov 2026 12:38:18 GMT | Count: 465 | bytes: 511525
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":465,"message":"Results returned successfully","results":[{"odiNumber":11775216,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/20/2025","dateComplaintFiled":"11/02/2026","vin":"1gnsktkl3mr","components":"ENGINE","summary":"Engine failure at2000miles, then at 80000","products":[{"type":"Vehicle","productYear":"2021","productMake":"CHEVROLET","productModel":"TAHOE","manufacturer":"General Motors, LLC"}]},{"odiNumber":11774400,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/23/2026","dateComplaintFiled":"10/29/2026","vin":"1GNSKMED6MR","components":"FUEL/PROPULSION SYSTEM","summary":"Fuel pump control module failed at under 60k miles. No parts in stock and was told by dealer, no parts anytime soon. This is unacceptable, especially since this is a known problem. A rental car should be provided as expected wait time is now going o
```
### recalls_Chevrolet_Tahoe_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2021`
- UTC time: 2026-11-04T12:38:18Z | HTTP Date: Wed, 04 Nov 2026 12:38:21 GMT | Count: 16 | bytes: 20834
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":16,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"21V455000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":true,"ReportReceivedDate":"17/06/2021","Component":"STEERING:STEERING CONTROL MODULE","Summary":"General Motors, LLC (GM) is recalling certain 2021 Cadillac Escalade, Escalade ESV, Chevrolet Suburban, Chevrolet Tahoe, GMC Yukon, and Yukon XL vehicles.  A software issue may cause a loss of power steering assist at startup or while driving.","Consequence":"Increased steering effort, particularly at lower speeds, increases the risk of a crash.","Remedy":"The power steering module software will be updated by a dealer, or through an over-the-air (OTA) update, free of charge.  Owner notification letters were mailed July 13, 2021.  Owners may contact Chevrolet customer service at 1-800-222-1020; Cadillac customer service at 1-800-458-8006; or GMC customer service at 1-800-462-8782.  GM's number for this r
```
### complaints_Chevrolet_Tahoe_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2021`
- UTC time: 2026-11-04T12:38:20Z | HTTP Date: Wed, 04 Nov 2026 12:38:24 GMT | Count: 465 | bytes: 511525
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":465,"message":"Results returned successfully","results":[{"odiNumber":11775216,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/20/2025","dateComplaintFiled":"11/02/2026","vin":"1gnsktkl3mr","components":"ENGINE","summary":"Engine failure at2000miles, then at 80000","products":[{"type":"Vehicle","productYear":"2021","productMake":"CHEVROLET","productModel":"TAHOE","manufacturer":"General Motors, LLC"}]},{"odiNumber":11774400,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/23/2026","dateComplaintFiled":"10/29/2026","vin":"1GNSKMED6MR","components":"FUEL/PROPULSION SYSTEM","summary":"Fuel pump control module failed at under 60k miles. No parts in stock and was told by dealer, no parts anytime soon. This is unacceptable, especially since this is a known problem. A rental car should be provided as expected wait time is now going o
```
### recalls_Chevrolet_Tahoe_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2022`
- UTC time: 2026-11-04T12:38:23Z | HTTP Date: Wed, 04 Nov 2026 12:38:26 GMT | Count: 4 | bytes: 5790
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"22V617000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"11/08/2022","Component":"SEAT BELTS:CRITICAL FASTENERS","Summary":"General Motors, LLC (M) is recalling certain 2021-2022 Cadillac Escalade, Escalade ESV, Chevrolet Suburban, Tahoe, GMC Yukon, and Yukon XL vehicles equipped with third-row seats.  The rivet that retains the buckle to the mounting bracket in the left or right side third-row seat belt buckle assembly may have been improperly formed.","Consequence":"A seat belt with a deformed rivet may not properly restrain an occupant, increasing the risk of injury during a crash.","Remedy":"Dealers will inspect the rivet head formation on both the left and right side third-row seat belt buckle assemblies and replace seat belt buckle assemblies, as necessary, free of charge.  Interim owner notification letters informing own
```
### complaints_Chevrolet_Tahoe_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2022`
- UTC time: 2026-11-04T12:38:25Z | HTTP Date: Wed, 04 Nov 2026 12:38:29 GMT | Count: 197 | bytes: 206363
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":197,"message":"Results returned successfully","results":[{"odiNumber":11772644,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"06/30/2026","dateComplaintFiled":"10/21/2026","vin":"1GNSKRKD6NR","components":"ENGINE","summary":"The dealership diagnosed the truck after investigating a ticking noise and engine misfire. During the inspection, they removed the valve cover and found that one of the pushrods on cylinder #5 was bent.  Further disassembly revealed that both lifters on cylinder #5 had failed, causing excessive wear on the camshaft lobe. As a result, the dealership determined that the necessary repair was to replace the camshaft and all 16 lifters.  The engine was then cleaned, reassembled, and tested to ensure proper operation. The root cause of the issue appears to have been a failing lifter, which led to damage of the associated valvetrain components.","products":[{"type":"Vehicle","productYear":
```
### recalls_Chevrolet_Tahoe_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2023`
- UTC time: 2026-11-04T12:38:29Z | HTTP Date: Wed, 04 Nov 2026 12:38:32 GMT | Count: 5 | bytes: 6946
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":5,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"22V903000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":true,"ReportReceivedDate":"08/12/2022","Component":"EXTERIOR LIGHTING:LIGHTING CONTROL MODULE:SOFTWARE","Summary":"General Motors, LLC (GM) is recalling certain 2020-2023 Cadillac CT4 and CT5; 2021-2023 Buick Envision; and 2022-2023 Cadillac Escalade and Escalade ESV, Chevrolet Silverado 1500, Suburban, Tahoe, GMC Sierra 1500, Yukon, and Yukon XL vehicles.  The daytime running lights (DRLs) may not deactivate when the headlights are on.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 108, \"Lamps, Reflective Devices, and Associated Equipment.\"","Consequence":"DRLs that do not deactivate as intended may result in a glare, reducing visibility, and increasing the risk of a crash.","Remedy":"The body control module software will be updated b
```
### complaints_Chevrolet_Tahoe_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Tahoe&modelYear=2023`
- UTC time: 2026-11-04T12:38:31Z | HTTP Date: Wed, 04 Nov 2026 12:38:35 GMT | Count: 234 | bytes: 259205
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":234,"message":"Results returned successfully","results":[{"odiNumber":11774593,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/03/2026","dateComplaintFiled":"10/30/2026","vin":"1GNSKTKL2PR","components":"ENGINE","summary":"I own a 2023 Chevrolet Tahoe equipped with the 6.2L V8 engine. The vehicle has experienced repeated significant engine problems, including a previous complete engine replacement and subsequent issues with the replacement engine.  The original engine required replacement due to engine-related problems. Following that replacement, the vehicle developed lifter noise and required another extended stay at the dealership for repairs. The vehicle has now been out of service for approximately 4–5 weeks while the dealership attempts to diagnose and repair the issue.  After the dealership completed work to address the lifter noise, the technician identified an additional concerning engine n
```
### probe_Honda_Pilot_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Pilot&modelYear=2021`
- UTC time: 2026-11-04T12:38:38Z | HTTP Date: Wed, 04 Nov 2026 12:38:44 GMT | Count: 454 | bytes: 481720
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":454,"message":"Results returned successfully","results":[{"odiNumber":11775001,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/01/2026","dateComplaintFiled":"11/01/2026","vin":"5FNYF5H20MB","components":"UNKNOWN OR OTHER,FORWARD COLLISION AVOIDANCE,LANE DEPARTURE","summary":"A cascade of warning errors suddenly appeared in my 2021 Honda Pilot. Lane keeping assist, adaptive cruise control, collission mitigation system, auto high bean, and road departure mitigation problem. The brake system light is also lit up. My mechanic said it is a \"millimeter wave error\" caused by one of the front cameras. After researching this, it seems that this is a common problem, and there is an active lawsuit.","products":[{"type":"Vehicle","productYear":"2021","productMake":"HONDA","productModel":"PILOT","manufacturer":"Honda (American Honda Motor Co.)"}]},{"odiNumber":11774608,"manufacturer":"Honda (America
```
### recalls_Honda_Pilot_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Pilot&modelYear=2021`
- UTC time: 2026-11-04T12:38:44Z | HTTP Date: Wed, 04 Nov 2026 12:38:47 GMT | Count: 10 | bytes: 13777
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":10,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"20V440000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"28/07/2020","Component":"ELECTRICAL SYSTEM:SOFTWARE","Summary":"Honda (American Honda Motor Co.) is recalling certain 2019-2021 Pilot, 2019-2020 Odyssey and 2019-2020 Passport vehicles.  Incorrect central network software programming may cause several errors to occur that can delay or prevent the rearview camera image from displaying.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard (FMVSS) number 111, \"Rearview Mirrors.\"","Consequence":"A delayed or inoperative rearview camera display can reduce the driver's view of what is behind the vehicle, increasing the risk of a crash.","Remedy":"Honda will notify owners that updated software is available.  Owners have the option to either follow the mailed instr
```
### complaints_Honda_Pilot_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Pilot&modelYear=2021`
- UTC time: 2026-11-04T12:38:46Z | HTTP Date: Wed, 04 Nov 2026 12:38:49 GMT | Count: 454 | bytes: 481720
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":454,"message":"Results returned successfully","results":[{"odiNumber":11775001,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"09/01/2026","dateComplaintFiled":"11/01/2026","vin":"5FNYF5H20MB","components":"UNKNOWN OR OTHER,FORWARD COLLISION AVOIDANCE,LANE DEPARTURE","summary":"A cascade of warning errors suddenly appeared in my 2021 Honda Pilot. Lane keeping assist, adaptive cruise control, collission mitigation system, auto high bean, and road departure mitigation problem. The brake system light is also lit up. My mechanic said it is a \"millimeter wave error\" caused by one of the front cameras. After researching this, it seems that this is a common problem, and there is an active lawsuit.","products":[{"type":"Vehicle","productYear":"2021","productMake":"HONDA","productModel":"PILOT","manufacturer":"Honda (American Honda Motor Co.)"}]},{"odiNumber":11774608,"manufacturer":"Honda (America
```
### recalls_Honda_Pilot_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Pilot&modelYear=2022`
- UTC time: 2026-11-04T12:38:49Z | HTTP Date: Wed, 04 Nov 2026 12:38:52 GMT | Count: 5 | bytes: 7095
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":5,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V431000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"15/06/2023","Component":"BACK OVER PREVENTION:DISPLAY FUNCTION","Summary":"Honda (American Honda Motor Co.) is recalling certain 2018-2023 Odyssey, 2019-2022 Pilot, and 2019-2023 Passport vehicles.  Due to a faulty Media Oriented Systems Transport (MOST) communication coaxial cable connector, the rearview camera image may not appear on the display.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 111, \"Rear Visibility.\"","Consequence":"A rearview camera that does not display an image can reduce the driver's rear view, increasing the risk of a crash or injury.","Remedy":"Dealers will replace the MOST cable harness and install a straightening cover over the vehicle cable connector, free of charge.  
```
### complaints_Honda_Pilot_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Pilot&modelYear=2022`
- UTC time: 2026-11-04T12:38:52Z | HTTP Date: Wed, 04 Nov 2026 12:38:55 GMT | Count: 174 | bytes: 190050
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":174,"message":"Results returned successfully","results":[{"odiNumber":11775150,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/26/2026","dateComplaintFiled":"11/02/2026","vin":"5FNYF5H24NB","components":"FORWARD COLLISION AVOIDANCE,LANE DEPARTURE","summary":"My vehicle started experience intermittent warnings on the dashboard stating that there was a lane keep assist problem, auto high beam problem, adaptive cruise control problem, brake system problem, among other things. I took it to the dealer and it got a code of U3000-49 and it needed a complete replacement coatings over $2,000. From online searches this appears to be a common problem with many Honda vehicles and raises a huge safety concern as it appears to be a defective piece of equipment that shuts down many safety features on my vehicle.","products":[{"type":"Vehicle","productYear":"2022","productMake":"HONDA","productModel":"PI
```
### recalls_Honda_Pilot_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Pilot&modelYear=2023`
- UTC time: 2026-11-04T12:38:54Z | HTTP Date: Wed, 04 Nov 2026 12:38:58 GMT | Count: 5 | bytes: 5589
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":5,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V735000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"02/11/2023","Component":"STEERING:RACK AND PINION:RACK","Summary":"Honda (American Honda Motor Co.) is recalling certain 2023-2024 Pilot vehicles.  Due to a manufacturing error, the gear box assembly may contain a loose ball bearing, which can result in a loss of steering control or steering lock-up.","Consequence":"A loss of steering control or steering lock-up can increase the risk of a crash.","Remedy":"Dealers will replace the electric power steering rack, free of charge.  Owner notification letters were mailed December 18, 2023.  Owners may contact Honda customer service at 1-888-234-2138.  Honda's number for this recall is FFX.","Notes":"Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (
```
### complaints_Honda_Pilot_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Pilot&modelYear=2023`
- UTC time: 2026-11-04T12:38:57Z | HTTP Date: Wed, 04 Nov 2026 12:39:01 GMT | Count: 149 | bytes: 160801
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":149,"message":"Results returned successfully","results":[{"odiNumber":11774646,"manufacturer":"Honda (American Honda Motor Co.)","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/21/2026","dateComplaintFiled":"10/30/2026","vin":"5FNYG1H85PB","components":"SEAT BELTS","summary":"The second-row passenger-side seat belt warning chime activates continuously even though the seat belt is properly fastened and the occupant is seated correctly. The vehicle indicates an unbuckled condition that does not exist. This is an intermittent problem. It does not occur on every trip, but once it starts, the warning chime continues for the entire trip while the vehicle is running or being driven, despite the belt being securely latched the whole time. Stopping and re-buckling does not reliably clear it. I have noticed a pattern in what triggers it: the warning most often begins when the vehicle turns left or right. The lateral movement of the occupant during
```
### probe_Kia_Sportage_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Kia&model=Sportage&modelYear=2021`
- UTC time: 2026-11-04T12:39:00Z | HTTP Date: Wed, 04 Nov 2026 12:39:04 GMT | Count: 54 | bytes: 52936
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":54,"message":"Results returned successfully","results":[{"odiNumber":11768470,"manufacturer":"Kia America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"05/15/2026","dateComplaintFiled":"10/02/2026","vin":"KNDPMCACXM7","components":"ENGINE AND ENGINE COOLING","summary":"The contact owns a 2021 Kia Sportage. The contact stated that after an oil change, while leaving the dealer and driving 55 MPH, there was an abnormal sound coming from the engine. The contact pulled over to the right side of the road, exited the vehicle, lifted the hood, and checked the oil dipstick and became aware that there was no oil on the dipstick. Since the failure, oil had been added to the engine three times. A dealer was contacted. The manufacturer was notified of the failure, opened a case, and informed the contact that the vehicle was out of warranty.  The approximate failure mileage was 103,916.","products":[{"type":"Vehicle","productYear":"2021","produc
```
### recalls_Kia_Sportage_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Kia&model=Sportage&modelYear=2021`
- UTC time: 2026-11-04T12:39:03Z | HTTP Date: Wed, 04 Nov 2026 12:39:07 GMT | Count: 2 | bytes: 2720
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":2,"Message":"Results returned successfully","results":[{"Manufacturer":"Kia Motors America","NHTSACampaignNumber":"21V137000","parkIt":false,"parkOutSide":true,"overTheAirUpdate":false,"ReportReceivedDate":"04/03/2021","Component":"SERVICE BRAKES, HYDRAULIC:ANTILOCK/TRACTION CONTROL/ELECTRONIC LIMITED SLIP:CONTROL UNIT/MODULE","Summary":"Kia Motors America (Kia) is recalling certain 2017-2021 Sportage and Cadenza vehicles.  The electrical circuit in the Hydraulic Electronic Control Unit (HECU) may short-circuit, which can cause a fire in the engine compartment.","Consequence":"An engine compartment fire can increase the risk of injury.","Remedy":"Owners are advised to park outside and away from structures as a precaution until the recall repair is complete.  Kia will notify owners, and dealers will replace certain fuses in the electrical junction box.  Vehicles equipped with an electronic parking brake (EPB) will also receive a HECU software update.  Repairs will be performed 
```
### complaints_Kia_Sportage_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Kia&model=Sportage&modelYear=2021`
- UTC time: 2026-11-04T12:39:07Z | HTTP Date: Wed, 04 Nov 2026 12:39:09 GMT | Count: 54 | bytes: 52936
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":54,"message":"Results returned successfully","results":[{"odiNumber":11768470,"manufacturer":"Kia America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"05/15/2026","dateComplaintFiled":"10/02/2026","vin":"KNDPMCACXM7","components":"ENGINE AND ENGINE COOLING","summary":"The contact owns a 2021 Kia Sportage. The contact stated that after an oil change, while leaving the dealer and driving 55 MPH, there was an abnormal sound coming from the engine. The contact pulled over to the right side of the road, exited the vehicle, lifted the hood, and checked the oil dipstick and became aware that there was no oil on the dipstick. Since the failure, oil had been added to the engine three times. A dealer was contacted. The manufacturer was notified of the failure, opened a case, and informed the contact that the vehicle was out of warranty.  The approximate failure mileage was 103,916.","products":[{"type":"Vehicle","productYear":"2021","produc
```
### recalls_Kia_Sportage_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Kia&model=Sportage&modelYear=2022`
- UTC time: 2026-11-04T12:39:08Z | HTTP Date: Wed, 04 Nov 2026 12:39:11 GMT | Count: 1 | bytes: 1403
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"Kia America, Inc.","NHTSACampaignNumber":"22V703000","parkIt":false,"parkOutSide":true,"overTheAirUpdate":false,"ReportReceivedDate":"19/09/2022","Component":"TRAILER HITCHES","Summary":"Kia America, Inc. (Kia) is recalling certain 2016-2022 Sorento, 2021-2022 Sorento Hybrid (HEV), 2022-2023 Sorento Plug-In Hybrid (PHEV), and 2017-2022 Sportage vehicles equipped with a tow hitch harness installed as original equipment, or purchased as an accessory through a Kia dealership.  Debris and moisture accumulation on the tow hitch harness module printed circuit board (PCB) may cause an electrical short, which can result in a fire.","Consequence":"A fire while parked or driving can increase the risk of injury.","Remedy":"Owners are advised to park outside and away from structures until the recall repair is complete.  Dealers will inspect the vehicle, and, as necessary, replace the fuse and/or tow hitch harness modu
```
### complaints_Kia_Sportage_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Kia&model=Sportage&modelYear=2022`
- UTC time: 2026-11-04T12:39:11Z | HTTP Date: Wed, 04 Nov 2026 12:39:13 GMT | Count: 47 | bytes: 50772
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":47,"message":"Results returned successfully","results":[{"odiNumber":11775012,"manufacturer":"Kia America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/09/2026","dateComplaintFiled":"11/01/2026","vin":"KNDPM3AC9N7","components":"ENGINE","summary":"I purchased my 2022 Kia Sportage in 2021 from Kia Store East here in [XXX].  On Oct. 9th, for the first time in five years, I saw an engine light on in my car and the car started shaking.  The dealer could not get me in until XXX.  I received a call on Oct. 22nd stating that the vehicle has a cylinder 1 misfire.  The dealership scoped the cylder one and found a hole in the exhaust valve.  The fix for a five year old car with 105K miles?  A long engine block replacement to the tune of $9,723.  There is an issue with these Kia engines that extends beyond the current settlement.  I was on the highway when this happened.  I could have easily been in an accident on the expressway.  The oil 
```
### recalls_Kia_Sportage_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Kia&model=Sportage&modelYear=2023`
- UTC time: 2026-11-04T12:39:13Z | HTTP Date: Wed, 04 Nov 2026 12:39:15 GMT | Count: 6 | bytes: 6613
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":6,"Message":"Results returned successfully","results":[{"Manufacturer":"Kia America, Inc.","NHTSACampaignNumber":"22V651000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"29/08/2022","Component":"ELECTRICAL SYSTEM:ALTERNATOR/GENERATOR/REGULATOR","Summary":"Kia America, Inc. (Kia) is recalling certain 2023 Sportage vehicles.  The alternator battery positive terminal nut may loosen, which can result in an engine stall or an electrical surge.","Consequence":"An engine stall increases the risk of a crash, and an electrical surge increases the risk of a fire.","Remedy":"Dealers will inspect and tighten the alternator battery positive terminal nut, as necessary, free of charge.  Owner notification letters were mailed September 23, 2022.  Owners may contact Kia customer service at 1-800-333-4542.  Kia's number for this recall is SC248.","Notes":"Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-8
```
### complaints_Kia_Sportage_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Kia&model=Sportage&modelYear=2023`
- UTC time: 2026-11-04T12:39:15Z | HTTP Date: Wed, 04 Nov 2026 12:39:18 GMT | Count: 196 | bytes: 201110
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":196,"message":"Results returned successfully","results":[{"odiNumber":11775289,"manufacturer":"Kia America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"11/02/2026","dateComplaintFiled":"11/02/2026","vin":"5XYK6CAF7PG","components":"UNKNOWN OR OTHER","summary":"I am filing a safety complaint regarding our 2023 Kia Sportage, VIN [XXX], with approximately 51,331 miles.  The vehicle began experiencing shaking and vibration while driving at speeds below approximately 40 mph. The check-engine warning light also illuminated. This raised serious concerns about the vehicle's reliability and safe operation, particularly because my daughter regularly drives this vehicle to and from school. I am concerned about the possibility of an unexpected loss of power, breakdown, or other mechanical failure while she is driving.  On XXX, the vehicle was inspected at Napleton's River Oaks Kia in [XXX]. According to Repair Order #XXX, diagnostic testing c
```
### probe_Subaru_Outback_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Outback&modelYear=2021`
- UTC time: 2026-11-04T12:39:18Z | HTTP Date: Wed, 04 Nov 2026 12:39:21 GMT | Count: 299 | bytes: 285256
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":299,"message":"Results returned successfully","results":[{"odiNumber":11773686,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"02/02/2026","dateComplaintFiled":"10/26/2026","vin":"4S4BTADC4M3","components":"VISIBILITY/WIPER","summary":"Windshield wiper fluid level sensor will not turn off even though reservoir is full","products":[{"type":"Vehicle","productYear":"2021","productMake":"SUBARU","productModel":"OUTBACK","manufacturer":"Subaru of America, Inc."}]},{"odiNumber":11771017,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/09/2026","dateComplaintFiled":"10/14/2026","vin":"4S4BTAPC4M3","components":"ELECTRICAL SYSTEM","summary":"Battery died multiple times. A DMC module went bad.","products":[{"type":"Vehicle","productYear":"2021","productMake":"SUBARU","productModel":"OUTBACK","manufacturer":"Subaru of America, Inc.
```
### recalls_Subaru_Outback_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Outback&modelYear=2021`
- UTC time: 2026-11-04T12:39:21Z | HTTP Date: Wed, 04 Nov 2026 12:39:24 GMT | Count: 4 | bytes: 4726
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Subaru of America, Inc.","NHTSACampaignNumber":"21V024000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"26/01/2021","Component":"POWER TRAIN:SHIFT LINKAGE/CABLE/ROD","Summary":"Subaru of America, Inc. (Subaru) is recalling certain 2021 Outback and Impreza vehicles.  The continuously variable transmission (CVT) select lever cable nut may not have been tightened properly, allowing the nut to loosen.","Consequence":"A loose nut can lead to a lost of retention in the CVT select lever cable and the gear selector not functioning properly, increasing risk of crash.","Remedy":"Subaru will notify owners, and dealers will inspect, and, if necessary, tighten the nut, free of charge.  The recall began February 12, 2021.  Owners may contact Subaru customer service at 1-844-373-6614.  Subaru's number for this recall is WRA-21.","Notes":"Owners may also contact the National Highway Tr
```
### complaints_Subaru_Outback_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Outback&modelYear=2021`
- UTC time: 2026-11-04T12:39:23Z | HTTP Date: Wed, 04 Nov 2026 12:39:26 GMT | Count: 299 | bytes: 285256
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":299,"message":"Results returned successfully","results":[{"odiNumber":11773686,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"02/02/2026","dateComplaintFiled":"10/26/2026","vin":"4S4BTADC4M3","components":"VISIBILITY/WIPER","summary":"Windshield wiper fluid level sensor will not turn off even though reservoir is full","products":[{"type":"Vehicle","productYear":"2021","productMake":"SUBARU","productModel":"OUTBACK","manufacturer":"Subaru of America, Inc."}]},{"odiNumber":11771017,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/09/2026","dateComplaintFiled":"10/14/2026","vin":"4S4BTAPC4M3","components":"ELECTRICAL SYSTEM","summary":"Battery died multiple times. A DMC module went bad.","products":[{"type":"Vehicle","productYear":"2021","productMake":"SUBARU","productModel":"OUTBACK","manufacturer":"Subaru of America, Inc.
```
### recalls_Subaru_Outback_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Outback&modelYear=2022`
- UTC time: 2026-11-04T12:39:26Z | HTTP Date: Wed, 04 Nov 2026 12:39:28 GMT | Count: 4 | bytes: 4528
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":4,"Message":"Results returned successfully","results":[{"Manufacturer":"Subaru of America, Inc.","NHTSACampaignNumber":"22V473000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"01/07/2022","Component":"ENGINE AND ENGINE COOLING:ENGINE:ENGINE CONTROL MODULE (ECU/ECM)","Summary":"Subaru of America, Inc. (Subaru) is recalling certain 2022 Outback vehicles.  The engine wiring harness may have been damaged, resulting in a loose electrical connection to the engine control unit (ECU).","Consequence":"A loose electrical connection to the ECU may cause an engine stall, increasing the risk of a crash.","Remedy":"Dealers will replace the engine wiring harness and ECU, free of charge.  Owner notification letters are expected to be mailed August 30, 2022.  Owners may contact Subaru's customer service at 1-844-373-6614.  Subaru's number for this recall is WRC-22.","Notes":"Owners may also contact the National Highway Traffic Safety Administration Vehicle 
```
### complaints_Subaru_Outback_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Outback&modelYear=2022`
- UTC time: 2026-11-04T12:39:28Z | HTTP Date: Wed, 04 Nov 2026 12:39:32 GMT | Count: 465 | bytes: 429062
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":465,"message":"Results returned successfully","results":[{"odiNumber":11769442,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/01/2026","dateComplaintFiled":"10/06/2026","vin":"4S4BTADCXN3","components":"ELECTRICAL SYSTEM,UNKNOWN OR OTHER,ENGINE","summary":"My Subaru often stalls when the start-stop function is happening such as when I stop at a traffic light. When I lift my foot off the break, the engine tries to restart, but stalls out. It happens at almost every stop. I had my battery tested and it is fine. This week, the car actually completely stalled out in heavy traffic and I had to put it in park and restart it.","products":[{"type":"Vehicle","productYear":"2022","productMake":"SUBARU","productModel":"OUTBACK","manufacturer":"Subaru of America, Inc."}]},{"odiNumber":11768004,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfI
```
### recalls_Subaru_Outback_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Subaru&model=Outback&modelYear=2023`
- UTC time: 2026-11-04T12:39:32Z | HTTP Date: Wed, 04 Nov 2026 12:39:36 GMT | Count: 2 | bytes: 2257
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":2,"Message":"Results returned successfully","results":[{"Manufacturer":"Subaru of America, Inc.","NHTSACampaignNumber":"23V647000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"21/09/2023","Component":"POWER TRAIN:DRIVELINE:DRIVESHAFT","Summary":"Subaru of America, Inc. (Subaru) is recalling certain 2023 Outback, Legacy, Ascent, and Impreza vehicles.  The center support bolts for the driveshaft may loosen, resulting in the disconnection of the front end of the driveshaft.","Consequence":"Separation of the front end of the driveshaft increases the risk of a crash.","Remedy":"Dealers will clean the bolt mounting surfaces of the center support brace and install new bolts, free of charge.  Owner notification letters were mailed November 20, 2023.  Owners may contact Subaru's customer service at 1-844-373-6614.  Subaru's number for this recall is WRN-23.","Notes":"Owners may also contact the National Highway Traffic Safety Administration Vehicle 
```
### complaints_Subaru_Outback_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Subaru&model=Outback&modelYear=2023`
- UTC time: 2026-11-04T12:39:35Z | HTTP Date: Wed, 04 Nov 2026 12:39:38 GMT | Count: 89 | bytes: 95788
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":89,"message":"Results returned successfully","results":[{"odiNumber":11761486,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"03/14/2026","dateComplaintFiled":"09/02/2026","vin":"4s4btgud3p3","components":"LANE DEPARTURE","summary":"While driving on the highway I had my cruise control on with my driving assist turned on. My car tried to veer to the left, hard, almost into the guardrail. It had happened before but not as severe as this time. Going highway speed, I was lucky enough no one was next to me. Someone could have got seriously injured!","products":[{"type":"Vehicle","productYear":"2023","productMake":"SUBARU","productModel":"OUTBACK","manufacturer":"Subaru of America, Inc."}]},{"odiNumber":11758281,"manufacturer":"Subaru of America, Inc.","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"08/18/2026","dateComplaintFiled":"08/20/2026","vin":"4S4BTGSD8P3","comp
```
### probe_Chevrolet_Traverse_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Traverse&modelYear=2021`
- UTC time: 2026-11-04T12:39:38Z | HTTP Date: Wed, 04 Nov 2026 12:39:41 GMT | Count: 94 | bytes: 89129
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":94,"message":"Results returned successfully","results":[{"odiNumber":11774524,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/14/2026","dateComplaintFiled":"10/29/2026","vin":"1GNEVJKW4MJ","components":"Carry Handle, Shell, Base,Other/I am not sure","summary":"In the upper right hand corner the plastic is starting to pull away. The seat belt is routed through this area.","products":[{"type":"Vehicle","productYear":"2021","productMake":"CHEVROLET","productModel":"TRAVERSE","manufacturer":"General Motors, LLC"},{"type":"Child Seat","productYear":"9999","productMake":"CHICCO","productModel":"FIT360","manufacturer":"Chicco USA, Inc."}]},{"odiNumber":11773753,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/21/2026","dateComplaintFiled":"10/26/2026","vin":"1GNEVKKW4MJ","components":"SERVICE BRAKES","summary":"The contact owns a 202
```
### recalls_Chevrolet_Traverse_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Traverse&modelYear=2021`
- UTC time: 2026-11-04T12:39:41Z | HTTP Date: Wed, 04 Nov 2026 12:39:44 GMT | Count: 3 | bytes: 3499
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":3,"Message":"Results returned successfully","results":[{"Manufacturer":"Braun Corporation","NHTSACampaignNumber":"21V817000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"18/10/2021","Component":"POWER TRAIN:AUTOMATIC TRANSMISSION","Summary":"Braun Corporation (Braun) is recalling certain 2020-2021 Chevrolet Traverse wheelchair accessible vehicles with Power In-floor Ramp conversion.  The screw and clip that hold the inner wheel-well plastic shroud in place may chafe against the transmission case, possibly resulting in a transmission fluid leak.","Consequence":"A transmission fluid leak can cause a loss of drive power, increasing the risk of a crash.  In addition, a leak in the presence of an ignition source increases the risk of a fire.","Remedy":"Dealers will replace the screw and clip, and inspect for signs of contact with the transmission, free of charge.  Owner notification letters were mailed November 29, 2021.  Owners may contact Brau
```
### complaints_Chevrolet_Traverse_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Traverse&modelYear=2021`
- UTC time: 2026-11-04T12:39:44Z | HTTP Date: Wed, 04 Nov 2026 12:39:47 GMT | Count: 94 | bytes: 89129
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":94,"message":"Results returned successfully","results":[{"odiNumber":11774524,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/14/2026","dateComplaintFiled":"10/29/2026","vin":"1GNEVJKW4MJ","components":"Carry Handle, Shell, Base,Other/I am not sure","summary":"In the upper right hand corner the plastic is starting to pull away. The seat belt is routed through this area.","products":[{"type":"Vehicle","productYear":"2021","productMake":"CHEVROLET","productModel":"TRAVERSE","manufacturer":"General Motors, LLC"},{"type":"Child Seat","productYear":"9999","productMake":"CHICCO","productModel":"FIT360","manufacturer":"Chicco USA, Inc."}]},{"odiNumber":11773753,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/21/2026","dateComplaintFiled":"10/26/2026","vin":"1GNEVKKW4MJ","components":"SERVICE BRAKES","summary":"The contact owns a 202
```
### recalls_Chevrolet_Traverse_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Traverse&modelYear=2022`
- UTC time: 2026-11-04T12:39:47Z | HTTP Date: Wed, 04 Nov 2026 12:39:50 GMT | Count: 1 | bytes: 1216
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":1,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"22V210000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"31/03/2022","Component":"AIR BAGS:SIDE/WINDOW:CURTAIN","Summary":"General Motors, LLC (GM) is recalling certain 2020-2022 Chevrolet Traverse and 2021-2022 Buick Enclave vehicles.  The harness connector to the left or right side roof rail air bag may have incompatible electrical terminals, which could prevent the air bags from deploying in a crash.","Consequence":"Roof rail air bags that do not deploy as intended increase the risk of injury in a crash.","Remedy":"Dealers will replace the harness connector to the roof rail air bags, free of charge.  Owner notification letters were mailed on April 29, 2022.  Owners may contact Buick customer service at 1-800-521-7300 or Chevrolet customer service at 1-800-222-1020.  GM's number for this recall is N212352140.","Notes":"Owners
```
### complaints_Chevrolet_Traverse_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Traverse&modelYear=2022`
- UTC time: 2026-11-04T12:39:49Z | HTTP Date: Wed, 04 Nov 2026 12:39:52 GMT | Count: 103 | bytes: 95982
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":103,"message":"Results returned successfully","results":[{"odiNumber":11774981,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/25/2026","dateComplaintFiled":"11/01/2026","vin":"1GNERFKW2NJ","components":"UNKNOWN OR OTHER","summary":"I am filing a formal safety complaint regarding an engineering defect in the exhaust support system of the 2022 Chevrolet Traverse that creates a direct chain-reaction failure, compromising vehicle safety and emissions controls. My vehicle experienced a complete structural failure of the front exhaust pipe mounting bracket—a known manufacturing defect heavily documented by General Motors under GM Special Coverage Adjustment N242445280. When this corporate-acknowledged bracket snaps, the exhaust system loses its vital structural anchoring point. As a direct mechanical consequence, the heavy catalytic converter assembly is left completely unsupported, subjecting it to viol
```
### recalls_Chevrolet_Traverse_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Chevrolet&model=Traverse&modelYear=2023`
- UTC time: 2026-11-04T12:39:52Z | HTTP Date: Wed, 04 Nov 2026 12:39:54 GMT | Count: 2 | bytes: 2533
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":2,"Message":"Results returned successfully","results":[{"Manufacturer":"General Motors, LLC","NHTSACampaignNumber":"23V042000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"02/02/2023","Component":"POWER TRAIN:DRIVELINE:DRIVESHAFT","Summary":"General Motors, LLC (GM) is recalling certain 2023 Chevrolet Blazer and Traverse vehicles.  The left-side half-shaft assemblies may be missing a retaining ring.","Consequence":"A missing retaining ring on the half-shaft can cause half-shaft inner joint separation, resulting in a loss of drive power or vehicle rollaway when the vehicle is placed in park.  Either of these scenarios can increase the risk of a crash.","Remedy":"Dealers will replace the left-side half-shaft assembly, free of charge.  Owner notification letters were mailed February 23, 2023.  Owners may contact Chevrolet customer service at 1-800-222-1020.  GM's number for this recall is N222390180.","Notes":"Owners may also contact the Natio
```
### complaints_Chevrolet_Traverse_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Traverse&modelYear=2023`
- UTC time: 2026-11-04T12:39:54Z | HTTP Date: Wed, 04 Nov 2026 12:39:57 GMT | Count: 95 | bytes: 92901
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":95,"message":"Results returned successfully","results":[{"odiNumber":11773683,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/24/2026","dateComplaintFiled":"10/26/2026","vin":"1GNEVNKW4PJ","components":"ELECTRICAL SYSTEM,UNKNOWN OR OTHER","summary":"Due to excessive current requirements being placed on it the alternator has failed at less than 31,000 miles. Replacements are unavailable and are excessively inflated at the dealership if available.","products":[{"type":"Vehicle","productYear":"2023","productMake":"CHEVROLET","productModel":"TRAVERSE","manufacturer":"General Motors, LLC"}]},{"odiNumber":11772765,"manufacturer":"General Motors, LLC","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"07/01/2026","dateComplaintFiled":"10/21/2026","vin":"1gnerhkw5pj","components":"POWER TRAIN","summary":"-The Torque Converter Clutch (TCC) inside the automatic transmission is 
```
### probe_Ford_Bronco_Sport_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2021`
- UTC time: 2026-11-04T12:39:56Z | HTTP Date: Wed, 04 Nov 2026 12:40:00 GMT | Count: 713 | bytes: 768122
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":713,"message":"Results returned successfully","results":[{"odiNumber":11774747,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/08/2026","dateComplaintFiled":"10/30/2026","vin":"3FMCR9C6XMR","components":"POWER TRAIN","summary":"I purchased a new 2021 Ford Bronco Sport, Model Outerbanks. The vehicle has had regular service at a Ford Dealership. In early October 2026 the Ford Dealership ran a diagnostic on the Bronco Sport and said the Rear Differential Unit (RDU) needed replaced. The estimated cost of the repair and parts was $4,000.00. The Ford warranty on the RDU is 5 years or 60,000 miles. My warranted ran out on September 21, 2026 and my mileage when diagnosed was 64,753.  Searching on the Ford Bronco Sport Internet Blog it appears the RDU issued is quite common requiring replacement on Bronco Sports with low and high mileage. It is clear that the RDU is either a bad design or poor product quality. 
```
### recalls_Ford_Bronco_Sport_2021
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2021`
- UTC time: 2026-11-04T12:40:00Z | HTTP Date: Wed, 04 Nov 2026 12:40:02 GMT | Count: 16 | bytes: 19378
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":16,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"21V074000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"16/02/2021","Component":"SUSPENSION:FRONT:CONTROL ARM","Summary":"Ford Motor Company (Ford) is recalling certain 2021 Bronco Sport vehicles.  These vehicles may have been produced with incorrect front lower control arms.","Consequence":"An incorrect lower control arm may affect vehicle handling and control, increasing the risk of a rollover crash.","Remedy":"Ford will notify owners, and dealers will inspect and replace the front lower control arms, if necessary, free of charge.  The recall began April 9, 2021.  Owners may contact Ford customer service at 1-866-436-7332.  Ford's number for this recall is 21S03.","Notes":"Owners may also contact the National Highway Traffic Safety Administration Vehicle Safety Hotline at 1-888-327-4236 (TTY 1-800-424-9153), or go to www.saf
```
### complaints_Ford_Bronco_Sport_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2021`
- UTC time: 2026-11-04T12:40:02Z | HTTP Date: Wed, 04 Nov 2026 12:40:06 GMT | Count: 713 | bytes: 768122
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":713,"message":"Results returned successfully","results":[{"odiNumber":11774747,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/08/2026","dateComplaintFiled":"10/30/2026","vin":"3FMCR9C6XMR","components":"POWER TRAIN","summary":"I purchased a new 2021 Ford Bronco Sport, Model Outerbanks. The vehicle has had regular service at a Ford Dealership. In early October 2026 the Ford Dealership ran a diagnostic on the Bronco Sport and said the Rear Differential Unit (RDU) needed replaced. The estimated cost of the repair and parts was $4,000.00. The Ford warranty on the RDU is 5 years or 60,000 miles. My warranted ran out on September 21, 2026 and my mileage when diagnosed was 64,753.  Searching on the Ford Bronco Sport Internet Blog it appears the RDU issued is quite common requiring replacement on Bronco Sports with low and high mileage. It is clear that the RDU is either a bad design or poor product quality. 
```
### recalls_Ford_Bronco_Sport_2022
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2022`
- UTC time: 2026-11-04T12:40:06Z | HTTP Date: Wed, 04 Nov 2026 12:40:10 GMT | Count: 15 | bytes: 18239
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":15,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"21V625000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"10/08/2021","Component":"FUEL SYSTEM, GASOLINE:DELIVERY:FUEL PUMP:CONTROL/DRIVE MODULE","Summary":"Ford Motor Company (Ford) is recalling certain 2021 Escape, Lincoln Corsair, and 2021-2022 Bronco Sport vehicles.  The fuel delivery module may leak inside the fuel tank, causing low fuel pressure which could result in an engine stall.","Consequence":"An engine stall increases the risk of a crash.","Remedy":"Dealers will replace the fuel delivery module, free of charge.  Interim notification letters (remedy not available) were mailed on September 30, 2021.  Owner notification letters were mailed on December 14, 2021.  Owners may contact Ford customer service at 1-866-436-7332.  Ford's number for this recall is 21S38.","Notes":"Owners may also contact the National Highway Tra
```
### complaints_Ford_Bronco_Sport_2022
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2022`
- UTC time: 2026-11-04T12:40:09Z | HTTP Date: Wed, 04 Nov 2026 12:40:13 GMT | Count: 370 | bytes: 394872
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":370,"message":"Results returned successfully","results":[{"odiNumber":11773229,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/23/2026","dateComplaintFiled":"10/23/2026","vin":"3FMCR9C62NR","components":"ENGINE,FUEL/PROPULSION SYSTEM","summary":"I am experiencing a fuel smell in my vehicle when I cold start it in the morning. I took it to the dealership and they could not identify the smell but claimed that if I call Ford customer service they might be able to escalate the issue. Ford customer service just said there is nothing they can do until the recall Campaign 25S76 is done but it is currently on pause even though it was issued 7/16/25 and it is currently 10/23/26. I said that these is a safety issue since Ford has identified that it can lead to the engine igniting which has happened to 8 vehicles according to Ford. They said they recommend waiting for the recall to happen despite my safety concer
```
### recalls_Ford_Bronco_Sport_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2023`
- UTC time: 2026-11-04T12:40:13Z | HTTP Date: Wed, 04 Nov 2026 12:40:16 GMT | Count: 14 | bytes: 16919
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":14,"Message":"Results returned successfully","results":[{"Manufacturer":"Ford Motor Company","NHTSACampaignNumber":"22V686000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"14/09/2022","Component":"EXTERIOR LIGHTING:LIGHTING CONTROL MODULE","Summary":"Ford Motor Company (Ford) is recalling certain 2022-2023 Bronco Sport and 2022 F-150 vehicles.  The parking lights may flicker when the headlights are activated.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard number 108, \"Lamps, Reflective Devices, and Associated Equipment.\"","Consequence":"Flickering parking lights can reduce visibility, increasing the risk of a crash.","Remedy":"Dealers will replace the LED Driver module, free of charge.  Owner notification letters were mailed March 29, 2023.  Owners may contact Ford customer service at 1-866-436-7332.  Ford's number for this recall is 22C22.","Notes":"Owners may also contact the Natio
```
### complaints_Ford_Bronco_Sport_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Ford&model=Bronco%20Sport&modelYear=2023`
- UTC time: 2026-11-04T12:40:16Z | HTTP Date: Wed, 04 Nov 2026 12:40:19 GMT | Count: 163 | bytes: 181011
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":163,"message":"Results returned successfully","results":[{"odiNumber":11773731,"manufacturer":"Ford Motor Company","crash":false,"fire":false,"numberOfInjuries":0,"numberOfDeaths":0,"dateOfIncident":"10/12/2026","dateComplaintFiled":"10/26/2026","vin":"3FMCR9D9XPR","components":"VISIBILITY/WIPER","summary":"My windshield wipers are randomly stopping working in the middle of driving in the rain. When the wipers stop, nothing on the lever is working, no rear wiper, no front wiper and no wiper fluid. The lever on the handle works nothing. This has happened probably 5 times randomly in last two weeks.  Once the wipers stopped in an upright position and lever wouldn’t do anything until i hit a bump in the road and they all of a sudden started working again. Very scary, very dangerous. I took it into FORD dealer and they said nothing was wrong after their diagnostics and they sent me on my way. Doing my own research into the problem i see a recall but not for my Bronco Sport. Plea
```
### recalls_Honda_Accord_2023
- Request: `api.nhtsa.gov/recalls/recallsByVehicle?make=Honda&model=Accord&modelYear=2023`
- UTC time: 2026-11-04T12:41:45Z | HTTP Date: Wed, 04 Nov 2026 12:41:48 GMT | Count: 5 | bytes: 6140
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"Count":5,"Message":"Results returned successfully","results":[{"Manufacturer":"Honda (American Honda Motor Co.)","NHTSACampaignNumber":"23V782000","parkIt":false,"parkOutSide":false,"overTheAirUpdate":false,"ReportReceivedDate":"21/11/2023","Component":"SEAT BELTS:FRONT","Summary":"Honda (American Honda Motor Co.) is recalling certain 2023-2024 Accord and HR-V vehicles.  The front seat belt pretensioners may be missing the rivet that secures the quick connector and wire plate.  As such, these vehicles fail to comply with the requirements of Federal Motor Vehicle Safety Standard numbers 208, \"Occupant Crash Protection,\" 209, \"Seat Belt Assembles,\" and 210, \"Seat Belt Assembly Anchorages.\"","Consequence":"A seat belt pretensioner missing a rivet will not properly restrain the occupant, increasing the risk of injury during a crash.","Remedy":"Dealers will inspect and replace the seat belt pretensioner assemblies as necessary, free of charge.  Owner notification letters were mailed
```
### complaints_Honda_Accord_2023
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Honda&model=Accord&modelYear=2023`
- UTC time: 2026-11-04T12:41:47Z | HTTP Date: Wed, 04 Nov 2026 12:41:52 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":0,"message":"Results returned successfully","results":[]}
```
### probe_Chevrolet_Silverado_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=Chevrolet&model=Silverado&modelYear=2021`
- UTC time: 2026-11-04T12:43:28Z | HTTP Date: Wed, 04 Nov 2026 12:43:31 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":0,"message":"Results returned successfully","results":[]}
```
### probe_GMC_Sierra_2021
- Request: `api.nhtsa.gov/complaints/complaintsByVehicle?make=GMC&model=Sierra&modelYear=2021`
- UTC time: 2026-11-04T12:43:30Z | HTTP Date: Wed, 04 Nov 2026 12:43:33 GMT | Count: 0 | bytes: 66
- Verbatim raw excerpt (first 1000 bytes, unmodified):
```text
{"count":0,"message":"Results returned successfully","results":[]}
```

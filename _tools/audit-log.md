# Accuracy audit log

Order: care_data2.py entries first (bulk written), top to bottom, then care_data.py. Sources: general hobby references (Seriously Fish / FishBase style ranges), kept conservative.

## 2026-10-08 (8 entries; care_data2.py entries 1-8)
- african-dwarf-frog: checked, OK.
- fire-belly-newt: checked, OK.
- paddletail-newt: checked, OK (trade fish are often mixed Pachytriton species; keep wording general).
- spanish-ribbed-newt: size corrected 9 in -> 8-10 in.
- shovelnose-catfish: CORRECTED. Size 24-40 in -> 24-48+ in, minimum tank 300 -> 500 gal, family Sorubim/Pseudoplatystoma now Pimelodidae text updated. Removed wrong merged aliases: redtail catfish (separate species, new guide redtail-catfish), sun catfish (Horabagrus, much smaller), gulper catfish / merodontotus tigrinus.
- serpae-tetra, bleeding-heart-tetra, buenos-aires-tetra: checked, OK.

Other fixes found during QA:
- neon-tetra aliases: removed green neon tetra, black neon tetra (separate species, now own guides) and candy cane tetra (unclear identity).
- fancy-goldfish aliases: removed bare "koi" (koi is a separate guide; a pond fish).
- neocaridina-shrimp: removed bare alias "shrimp" (hijacked ghost shrimp and any shrimp).
- echinodorus-varieties: removed Sagittaria aliases (different genus); dwarf sagittaria now own guide.
- rainbowfish: removed "dwarf neon rainbowfish" (own guide). STILL TO REVIEW: this guide lumps many species (4 in, 30 gal) incl. threadfin, celebes, madagascar, featherfin; split later.

Next up: care_data2.py from flame-tetra onward.

## 2026-10-09 (8 entries; care_data2.py entries 9-16)
- flame-tetra, penguin-tetra, black-phantom-tetra, red-phantom-tetra, bloodfin-tetra, glofish-tetra, emperor-tetra: checked, OK.
- diamond-tetra: minimum tank 20 -> 30 gal (active 2.5 in schooling fish, group of 6+).
- synodontis-catfish: removed alias "upside down catfish" (that is S. nigriventris, now its own guide).
Next up: care_data2.py after emperor-tetra.

## 2026-10-10 (8 entries; care_data2.py entries 17-24)
- blue-tetra: removed aliases "columbian tetra"/"colombian tetra" (separate species, own guide).
- bucktooth-tetra: minimum tank 40 -> 55 gal (group of 6+, 4-5 in); size 4 -> 4-5 in.
- silver-tip-tetra: temperature 68-82 -> 70-80 F (conservative).
- hatchetfish: size 2 in -> 1-2.5 in (pygmy to silver hatchets are lumped).
- strawberry-rasbora, pygmy-rasbora: minimum tank 5 -> 10 gal for the 8+ group.
- clown-rasbora, espei-rasbora: checked, OK.
Next up: care_data2.py from giant-danio onward.

## 2026-10-11 (8 entries; care_data2.py entries 25-32)
- giant-danio: size 4 in -> 4-6 in, minimum tank 30 -> 40 gal, temperature 65-80 -> 68-78 F (active 6-in schooling fish).
- rosy-barb: size 3 -> 3-4 in, minimum tank 20 -> 30 gal (active group of 6+).
- denison-barb: size 4.5 -> 4-6 in (wild fish reach about 6 in).
- tinfoil-barb: size 12 -> 10-14 in, minimum tank 125 -> 200 gal (group of 4+ of 12-in fish), temperature 72-77 -> 72-79 F.
- leopard-danio, odessa-barb, ruby-barb, gold-barb: checked, OK.
- licorice-gourami: removed wrong aliases (thicklip sunset gourami, pygmy gourami, samurai gourami, croaking gourami); lotus-tiger: removed Nymphoides aliases (banana plant is a different plant, now its own guide).
Next up: care_data2.py from bala-shark onward.

## 2026-10-12 (8 entries; care_data2.py entries 33-40)
- bala-shark: size 12 -> 12-14 in, minimum tank 150 -> 180 gal (group of 3+ of 12-in fish).
- rainbow-shark, red-tail-black-shark, flying-fox, chinese-algae-eater, medaka, limia, julii-cory: checked, OK.
Next up: care_data2.py after julii-cory.

## 2026-10-13 (8 entries; care_data2.py entries 41-48)
- sterbai-cory, pygmy-cory, skunk-cory, albino-cory, corydoras-assorted, common-pleco, clown-pleco: checked against SeriouslyFish/Wikipedia/Tankarium/AquariumSource, all OK (common-pleco's 15 in captive-size and 125 gal tank sit correctly between sources' 75-80 gal minimum and 150 gal ideal; clown-pleco's 4 in/73-82F matches Tankarium's 3-4 in/73-82F).
- golden-nugget-pleco: sources disagree sharply (SeriouslyFish: max 180mm/~7in SL, needs 81-90F; AquariumSource: up to 10 in, 73-79F) — likely the same lumped-trade-name problem seen elsewhere in this audit (L018/L081 "gold nugget" covers more than one similar Baryancistrus/Scobinancistrus species). This entry's existing 7 in/78-86F/55 gal already sits as a defensible middle ground between the conflicting sources; left as-is rather than picking one source as ground truth.
Next up: care_data2.py from whiptail-catfish onward. (done on 2026-10-13b below)

## 2026-10-13 second pass (8 entries; care_data2.py entries 49-56)
- synodontis-catfish: pH 7.0-8.5 -> 6.5-8.5 (several common species, e.g. the upside-down type, do fine near neutral).
- yoyo-loach: minimum tank 40 -> 55 gal, group "3+" -> "5+" (active social loach; small groups cause bullying).
- whiptail-catfish, hoplo-catfish, pictus-catfish, raphael-catfish, banjo-catfish, dojo-loach: checked against general hobby references, OK.
Next up: care_data2.py from zebra-loach onward.

## 2026-10-14 (8 entries; care_data2.py entries 57-64)
- horseface-loach: minimum tank 40 -> 55 gal (8-in burrower that needs floor space).
- flame-gourami: same species as dwarf-gourami (Trichogaster lalius), so difficulty Beginner -> Intermediate and temperature 72-82 -> 74-82 F to match; added quarantine/disease tip.
- zebra-loach, hillstream-loach, botia-loach, dwarf-chain-loach, giant-gourami, opaline-gourami: checked against general hobby references, OK.
Next up: care_data2.py after flame-gourami (licorice-gourami was audited earlier; continue with the entries following it in file order that are not yet logged).

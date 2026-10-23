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

## 2026-10-15 (8 entries; care_data2.py: x-ray-tetra .. severum)
- emerald-dwarf-rasbora: scientific name corrected Danionella erythromicron -> Danio erythromicron (Danionella is a different genus); size 0.8 -> 0.8-1 in.
- severum: size 8 -> 8-10 in.
- x-ray-tetra, melon-barb, zebra-pleco, royal-pleco, paradise-fish, plakat-betta: checked against general hobby references, OK.
- Alias bug: "lagenandra meeboldii"/"lagenandra bleeding heart" were hidden inside bucephalandra-varieties (different genus); moved to the new lagenandra guide.
Next up: care_data2.py from geophagus onward (see list of unlogged slugs: python check vs this file).

## 2026-10-17 (8 entries; care_data2.py: fahaka-puffer .. red-belly-pacu)
- fahaka-puffer: lifespan 10+ -> 15-20 years (multiple sources agree captive fahakas commonly live well past 10 years with proper care).
- bichir (genus-level): minimum tank 75 -> 90 gal (AquariumSource recommends ~90 gal for one fish of the larger species in this lumped entry, e.g. P. endlicheri).
- knifefish (lumped Chitala/Notopterus/related): minimum tank 75 -> 250 gal. The entry's own size range already goes to 36 in (adult clown knifefish), and a 75 gal tank badly undersold that; added a tip calling out the adult clown knifefish by name so buyers of the small juvenile understand the real commitment.
- elephant-nose-fish: minimum tank 55 -> 75 gal (Aquariadise/ThatPetPlace both recommend 75-120 gal for a solitary territorial fish this size; split the difference conservatively rather than jump straight to the higher figure).
- silver-dollar: minimum tank 55 -> 75 gal (Tankflare's species profile gives 75 gal as the cycled minimum for a schooling group of 5+).
- red-belly-pacu: size 24 in -> 24-35 in, minimum tank 400 -> 700 gal. SeriouslyFish lists wild fish to 35 in and a ~2,550-liter (~674 US gal) footprint as the real minimum for an adult; the old 24 in/400 gal figures were a significant undersell for a fish this site already (correctly) calls "not suitable for most homes."
- mbu-puffer: checked against AquariumSource (22-30+ in, 500 gal minimum/1,000 preferred, 75-79°F, pH 7.0-8.0 ideal 7.5, ~10 yr lifespan) — site's existing 26 in/500 gal/75-82°F/7.0-8.0/10+ yr figures all sit within or match that range, no change needed.
Next up: care_data2.py from datnoid onward.

## 2026-10-16 (8 entries; care_data2.py: peacock-bass .. green-spotted-puffer)
- green-spotted-puffer: minimum tank 30 -> 55 gal, size 6 -> 6-7 in, tip now says adults need brackish to near-marine water (messy, long-lived).
- peacock-bass: size 20 in -> 12-28 in by species, tip that the biggest species need far more than 300 gal.
- tropheus: minimum tank 75 -> 100 gal, group "large" -> 8-12+ (small groups bully the weakest fish).
- firemouth-cichlid: size 6 -> 5-6 in. multies-shell-dweller: size 2 -> 1-2 in (shells are the colony unit).
- blood-parrot-cichlid, uaru, german-gold-ram, apistogramma (genus-level), electric-blue-jack-dempsey: checked against general hobby references, OK.
Next up: care_data2.py after electric-blue-jack-dempsey (67 entries unlogged by slug; see check script in README).

## 2026-10-17b (8 entries; care_data2.py: datnoid .. ramshorn-snail)
- datnoid: size 18 -> 16-20 in; added note that it passes a foot quickly and needs a 6-ft tank.
- gar: noted that "hujeta gar"/"freshwater barracuda" aliases are pike characins (smaller than true gar) and that alligator gar reach 6 ft+ (pond-only; CA status to confirm).
- pencilfish: size 2 -> 1.5-2.5 in (species vary), minimum tank 10 -> 15 gal for a group of 6+ (SeriouslyFish-type bases are ~14 gal).
- assassin-snail: added that it sometimes eats nerites and breeds slowly.
- ramshorn-snail: size 0.5 -> 0.5-1 in (red/giant forms).
- dwarf-puffer-specialty: note now warns that fugu-type puffers may need brackish water as adults and Congo/Amazon puffers reach 5-6 in.
- arowana-other, killifish: checked against general hobby references, OK.
Next up: care_data2.py from trapdoor-snail onward (python check vs this file).

## 2026-10-18 (8 entries; care_data2.py: rabbit-snail .. clam-freshwater)
NOTE: WebFetch was blocked today (permission prompts unanswered) and WebSearch returns only titles/links, so these checks are from general hobby knowledge, not re-verified against a fetched page.
- rabbit-snail: size 3 -> 3-4 in, minimum tank 10 -> 15 gal (large snails, heavy bioload for a colony).
- inca-snail, bamboo-shrimp, neocaridina-color-shrimp: checked against general hobby ranges, OK.
- crayfish: FLAG for Roger. Live crayfish are heavily restricted in California; the guide should probably be removed unless Pet Zone has confirmed legal stock. Not changed.
- freshwater-crab: FLAG. Lumps small Geosesarma with large Cardisoma land crabs (4+ in); CA status unclear. Not changed.
- hermit-crab-freshwater: marine species (Clibanarius) kept as an honest "not freshwater" warning guide; OK.
- clam-freshwater: FLAG. Corbicula is a widely regulated invasive clam in many US states; confirm California status. Not changed.
Next up: care_data2.py from bacopa-caroliniana onward.

## 2026-10-19 (8 entries; care_data2.py: ludwigia-red .. hornwort)
NOTE: no fetched sources today (WebSearch returns titles only); checks are from general hobby/plant references.
- pogostemon-helferi: removed "pogostemon stellata octopus"/"pogostemon octopus" aliases (Octopus is a stellatus form); moved to pogostemon-stellatus.
- hygrophila: removed nomaphila stricta/siamensis/variegatus aliases; moved to the nomaphila guide.
- ludwigia-red, alternanthera-reineckii, staurogyne-repens, dwarf-baby-tears, micro-sword, hornwort: ranges, family and size checked, OK. (dwarf-baby-tears CO2 "Required" is the conservative call.)
Next up: care_data2.py from water-lettuce onward (CA noxious-weed flags for water-lettuce, parrots-feather, anacharis-egeria remain open for Roger).

## 2026-10-20 (8 entries; care_data2.py: water-lettuce .. cryptocoryne-parva)
NOTE: WebFetch blocked again (permission prompt unanswered); checks from general hobby/plant knowledge, not re-verified against fetched pages.
- water-lettuce: values OK; FLAG for Roger again: Pistia stratiotes is regulated as a noxious weed in California, so confirm Pet Zone may sell it before keeping the guide.
- salvinia: removed misfit aliases "water mimosa" / "sensitive plant floater" (a different plant, Neptunia). Dwarf-vs-giant salvinia note kept.
- red-root-floater: checked, OK.
- christmas-moss: origin "Southeast Asia" -> "Tropical regions (often sold as an Asian moss)"; the species is not strictly Asian.
- marimo-moss-ball, java-fern-varieties, bolbitis: checked, OK (bolbitis can pass 14 in in good conditions).
- cryptocoryne-parva: BUG FIXED. It lumped about 30 crypt names, including large species (usteriana, spiralis, retrospiralis, undulata) and wendtii forms, under a 2-4 in foreground crypt. Now only parva/pygmaea/lucens; wendtii forms moved to cryptocoryne-wendtii; other species moved to the new cryptocoryne-varieties guide (4-24 in, by species). Also removed "cryptocoryne undulata" from the lutea guide (different species).
Next up: care_data2.py from anubias-varieties onward.

## 2026-10-21 (8 entries; care_data2.py: anubias-varieties .. ammannia)
NOTE: WebSearch returns titles only and WebFetch is not usable unattended, so checks are from general hobby/plant knowledge.
- echinodorus-varieties: removed helanthium/tenellus/pygmy chain sword aliases (3-4 in foreground plant, has its own guide).
- rotala-varieties: moved "rotala bonsai" alias to ammannia (Ammannia sp. Bonsai).
- aponogeton: description and tips now warn that Madagascar lace is advanced (soft, clean, cooler water) while crispus/ulvaceus are easy.
- anubias-varieties, vallisneria-varieties, marsilea, hydrocotyle, ammannia: ranges checked, OK. Note: floating marsh pennywort (H. ranunculoides) is a CA-regulated weed and is not aliased.
Next up: care_data2.py from eleocharis onward.

## 2026-10-22 (8 entries; care_data2.py: eleocharis .. amazon-frogbit-floaters region, first 8 = eleocharis .. bucephalandra-varieties)
NOTE: no fetched sources (WebFetch blocked, search titles only); checks from general hobby/plant knowledge.
- bucephalandra-varieties: BUG FIXED, removed "barclaya"/"barclaya longifolia" aliases (they hijacked the Barclaya guide, a different plant). Test added.
- whiptail-catfish: removed "royal farlowella catfish" alias (Sturisoma is larger, now its own guide).
- parrots-feather: removed "foxtail" and "watermilfoil" aliases (ambiguous with hornwort / invasive spicatum). CA weed status of Myriophyllum aquaticum still open for Roger.
- eleocharis: removed "eleocharis vivipara" alias (grows much taller than the 2-8 in range).
- lotus-tiger: removed "dwarf lily" alias (own dwarf water lily guide); height 8-20 in -> 10-24 in.
- najas-guppy-grass, limnophila, mayaca, pothos-emersed: ranges checked, OK.
Next up: care_data2.py from anacharis-egeria onward.

## 2026-10-23 (8 entries; care_data2.py: anacharis-egeria .. tissue-culture-plant, then care_data3.py first 5)
NOTE: no fetched care sources (WebFetch only reached the Pet Zone sitemap); checks from general hobby knowledge. care_data2.py is now fully audited once.
- amazon-frogbit-floaters: BUG FIXED, removed aliases "ranalisma rostratum" (new own guide), "rorippa aquatica" (lake cress guide) and "penthorum sedoides" (not a floater).
- anacharis-egeria: ranges OK. FLAG for Roger: Egeria densa is a California-regulated noxious weed (like water lettuce); same decision as before applies.
- tissue-culture-plant: OK.
- green-neon-tetra: removed claim of a red area on the body (Paracheirodon simulans has none); text now says no red.
- black-neon-tetra, redtail-catfish, ghost-shrimp, emerald-catfish: checked, OK.
- gar: removed "spotted pike characin false gar" alias (a Boulengerella, now pike-characin).
Next up: care_data3.py from dwarf-neon-rainbowfish onward.

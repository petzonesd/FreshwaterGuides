# Batch 3 (2026-10-08): more species Pet Zone sells. Original text; conservative general-hobby ranges.
from care_data import A, P

MORE_ANIMALS = [
 A("black-neon-tetra","Black Neon Tetra","Hyphessobrycon herbertaxelrodi","fish","Characidae","Paraguay River basin, South America","1.75 in",(72,79),(5.5,7.5),15,"Peaceful","Schooling, keep 6+","Mid","Beginner","Omnivore: micro pellets, flakes, frozen foods","3-4 years",
  "A small, hardy tetra with a white-edged black body stripe. It is a different species from the common neon tetra, with its own look and slightly different water preferences, and it does well in a planted community tank.",
  ["Keep a group of six or more.","Not a neon tetra; do not rely on neon care notes for exact numbers.","Choose calm, small tankmates."],aka=["black neon tetras","black neon","hyphessobrycon herbertaxelrodi"]),
 A("green-neon-tetra","Green Neon Tetra","Paracheirodon simulans","fish","Characidae","Rio Negro and Orinoco basins, South America","1.25 in",(73,82),(5.5,7.0),10,"Peaceful, shy","Schooling, keep 8+","Mid","Intermediate","Micro pellets, crushed flakes, baby brine shrimp, small frozen foods","3-4 years",
  "A tiny cousin of the neon tetra with a green-blue stripe and a short red area at the tail. It is smaller and shyer than a neon and prefers softer, clean, stable water in a quiet planted tank.",
  ["Keep a group of eight or more.","Only pair with small, gentle tankmates.","Make changes to the water slowly."],aka=["green neon tetras","green neon","paracheirodon simulans"]),
 A("redtail-catfish","Redtail Catfish","Phractocephalus hemioliopterus","fish","Pimelodidae","Amazon and Orinoco basins, South America","36-48+ in",(72,82),(6.0,7.5),1000,"Predatory, will eat anything that fits","Solitary","Bottom to mid","Advanced","Carnivore: fish, shrimp, squid, large sinking pellets","15-20+ years",
  "Sold as a cute juvenile, the redtail catfish grows into a heavy, powerful fish about three to four feet long. It needs a tank measured in the high hundreds or thousands of gallons, which is why it is usually a fish for a public aquarium or a pond-sized setup.",
  ["Plan for a tank of 1,000 gallons or more before buying.","Do not keep with any fish small enough to swallow.","Use heavy equipment covers and strong filtration."],aka=["red tail catfish","redtail cat","red tailed catfish","red tail cat","phractocephalus hemioliopterus","phractocephalus hemiliopterus","redtail catfish phractocephalus hemioliopterus","redtail catfish phractocephalus"]),
 A("ghost-shrimp","Ghost Shrimp","Palaemonetes paludosus","invert","Palaemonidae","Southeastern United States","1.5-2 in",(68,82),(6.5,8.0),5,"Peaceful, but may eat tiny shrimp and fry","Groups of 3+","All levels","Beginner","Omnivore: algae wafers, sinking pellets, leftover food, biofilm","1-2 years",
  "A see-through freshwater shrimp that cleans up scraps and is fun to watch. It lives only about a year or two, and it is larger and more predatory than cherry shrimp, so do not count on baby shrimp surviving in the same tank.",
  ["Avoid copper-based medications.","Provide hiding spots for molting.","Do not mix with tiny shrimp you want to breed."],aka=["ghost shrimps","glass shrimp","palaemonetes","palaemonetes paludosus","ghost shrimp feeder"]),
 A("emerald-catfish","Emerald Catfish","Brochis splendens","fish","Callichthyidae","Upper Amazon basin, South America","3 in",(72,79),(6.0,7.5),30,"Peaceful","Groups of 5+","Bottom","Beginner","Omnivore: sinking pellets and wafers, frozen foods","8-10 years",
  "A shimmering green armored catfish that is taller and longer than most corydoras. Keep a group on soft sand or smooth gravel and feed foods that sink.",
  ["Keep five or more together.","Use smooth sand or fine gravel.","Needs a larger tank than small corydoras."],aka=["emerald green cory","emerald cory","emerald corydoras","corydoras splendens","short body catfish","brochis splendens","emerald green catfish"]),
 A("dwarf-neon-rainbowfish","Dwarf Neon Rainbowfish","Melanotaenia praecox","fish","Melanotaeniidae","Northern New Guinea","3 in",(74,80),(6.5,7.8),20,"Peaceful, active","Schooling, keep 6+","Upper to mid","Beginner","Omnivore: micro pellets, flakes, frozen foods","4-5 years",
  "A small, bright rainbowfish with a blue body and red fins. It is a good fit for medium community tanks, needs a group and open swimming space, and does best in clean, moderately hard water.",
  ["Keep a group of six or more.","Use a tight lid; rainbowfish jump.","Feed small portions, twice a day."],aka=["dwarf neon rainbow","neon dwarf rainbowfish","praecox rainbowfish","melanotaenia praecox"]),
 A("blue-acara","Blue Acara","Andinoacara pulcher","fish","Cichlidae","Panama, Colombia and Venezuela","6-8 in",(72,82),(6.5,7.8),55,"Semi-aggressive, territorial when breeding","Pair or solitary","Bottom to mid","Intermediate","Omnivore: cichlid pellets, frozen foods, vegetables","8-10 years",
  "A hardy, medium-sized cichlid with blue-green markings. It is calmer than most large cichlids but will eat small fish and defend a territory when breeding.",
  ["Do not keep with small fish like neons.","Provide caves and open swimming space.","Use a sturdy lid and strong filtration."],aka=["blue acara cichlid","andinoacara pulcher","aequidens pulcher","electric blue acara"]),
 A("keyhole-cichlid","Keyhole Cichlid","Cleithracara maronii","fish","Cichlidae","The Guianas, South America","4 in",(72,80),(6.0,7.5),30,"Peaceful, shy","Pairs or small groups","Bottom to mid","Intermediate","Omnivore: small pellets, frozen foods, live foods","8-10 years",
  "A calm, shy cichlid named for the keyhole-shaped dark mark on its side. It does best in a quiet tank with plants, caves and gentle tankmates.",
  ["Use calm tankmates; boisterous fish stress it.","Provide caves and plants.","Keep water clean and stable."],aka=["keyhole cichlids","cleithracara maronii","keyhole cichlid cleithracara maronii"]),
 A("sparkling-gourami","Sparkling Gourami","Trichopsis pumila","fish","Osphronemidae","Southeast Asia","1.5 in",(72,82),(6.0,7.5),10,"Peaceful, shy","Pairs or small groups","Upper to mid","Intermediate","Carnivore: micro pellets, baby brine shrimp, small frozen foods","3-4 years",
  "A tiny labyrinth fish with iridescent dots and the ability to make soft croaking sounds. It needs a calm, planted tank with floating plants and very gentle tankmates.",
  ["Leave an air gap under the lid.","Use floating plants for cover.","Feed tiny live or frozen foods."],aka=["sparkling gouramis","croaking gourami","trichopsis pumila"]),
 A("pearl-danio","Pearl Danio","Danio albolineatus","fish","Danionidae","Thailand, Myanmar and Sumatra","2.5 in",(68,79),(6.0,8.0),20,"Peaceful, very active","Schooling, keep 6+","Upper to mid","Beginner","Omnivore: flakes, micro pellets, frozen foods","3-5 years",
  "A fast, hardy schooling danio with a pearly sheen and a hint of pink or blue. It needs a long tank with open water and a secure lid.",
  ["Keep a group of six or more.","Use a tight lid; danios jump.","Choose a tank that is at least two feet long."],aka=["pearl danios","danio albolineatus","pearly danio"]),
 A("red-eye-tetra","Red Eye Tetra","Moenkhausia sanctaefilomenae","fish","Characidae","Paraguay River basin, South America","2.5 in",(72,80),(6.0,7.5),20,"Active, mostly peaceful, may nip long fins","Schooling, keep 6+","Mid to upper","Beginner","Omnivore: flakes, micro pellets, frozen foods","4-5 years",
  "A silver tetra with a red ring above the eye. Hardy and active, it likes to be in a group and may nibble the fins of long-finned fish.",
  ["Keep a group of six or more.","Avoid long-finned tankmates.","Tough plants work best; it can nibble soft ones."],aka=["red eye tetras","redeye tetra","moenkhausia sanctaefilomenae","red eyed tetra"]),
 A("checker-barb","Checker Barb","Oliotius oligolepis","fish","Cyprinidae","Sumatra and nearby islands, Indonesia","2 in",(68,77),(6.0,7.5),20,"Peaceful, active","Schooling, keep 6+","Mid to lower","Beginner","Omnivore: flakes, micro pellets, frozen foods","4-5 years",
  "A small, peaceful barb with a checkered scale pattern and orange-tinged fins on the males. It is hardy, likes cooler water than many tropical fish, and is a calm pick for community tanks.",
  ["Keep a group of six or more.","Tolerates cooler tropical temperatures.","Use a lid; barbs can jump."],aka=["checkered barb","checker barbs","oliotius oligolepis","puntius oligolepis","island barb"]),
]

MORE_PLANTS = [
 P("dwarf-sagittaria","Dwarf Sagittaria","Sagittaria subulata","Alismataceae","Eastern Americas","2-10 in","Low to medium","Optional","Foreground to midground","Medium",(65,82),(6.0,7.5),"Beginner","Runners",
  "A grass-like plant that sends out runners and carpets the front of a tank. It grows taller in strong light, so trim to keep it low.",
  ["Plant the crown at substrate level, not buried.","Root tabs help it spread.","Trim tall leaves to keep it as a carpet."],aka=["sagittaria subulata","dwarf sag","dwarf sagittaria subulata","dwarf sagittaria sagittaria subulata"]),
 P("water-sprite","Water Sprite","Ceratopteris thalictroides","Pteridaceae","Tropical regions worldwide","6-20 in","Low to high","Not needed","Planted or floating","Fast",(68,82),(6.0,7.5),"Beginner","Plantlets and cuttings",
  "A fast, feathery fern that soaks up nutrients quickly and gives fry and shy fish cover. It can be planted in the substrate or left floating.",
  ["Remove or replant the baby plantlets that form on old leaves.","Floating plants soften the light for fish that like shade.","Trim often to keep it from shading other plants."],aka=["water sprite plant","ceratopteris thalictroides","indian fern","oriental water sprite"]),
]

ALIAS_INTO = {}

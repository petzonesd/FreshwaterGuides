# Original care dataset for Pet Zone care labels / care pages.
# Ranges are conservative, general-hobby figures written for Pet Zone's own use.
# Fields (animals): slug,name,sci,kind,family,origin,size,temp,ph,tank,temperament,social,level,difficulty,diet,life,note,tips
# kind: fish | invert.  Plants use P(...) below.

def A(slug, name, sci, kind, family, origin, size, temp, ph, tank, temperament, social, level, difficulty, diet, life, note, tips, aka=()):
    return dict(slug=slug, name=name, sci=sci, kind=kind, family=family, origin=origin, size=size, temp=temp, ph=ph,
                tank=tank, temperament=temperament, social=social, level=level, difficulty=difficulty, diet=diet,
                life=life, note=note, tips=list(tips), aka=list(aka))

def P(slug, name, sci, family, origin, height, light, co2, placement, growth, temp, ph, difficulty, propagation, note, tips, aka=()):
    return dict(slug=slug, name=name, sci=sci, kind="plant", family=family, origin=origin, height=height, light=light,
                co2=co2, placement=placement, growth=growth, temp=temp, ph=ph, difficulty=difficulty,
                propagation=propagation, note=note, tips=list(tips), aka=list(aka))

ANIMALS = [
 # ---------------- Tetras ----------------
 A("neon-tetra","Neon Tetra","Paracheirodon innesi","fish","Characidae","Amazon basin, South America","1.5 in",(72,78),(6.0,7.5),10,"Peaceful","Schooling, keep 6+","Mid to upper","Beginner","Omnivore: micro pellets and flakes","3-5 years",
   "A small, calm schooling fish that shows its best color in a group of six or more. Captive-bred fish are hardier than wild ones, but they still prefer stable water over big swings.",
   ["Add them after the tank has fully cycled.","Keep 6 or more so they school instead of hiding.","Avoid big, mouthy tankmates that see them as snacks."],aka=["neons"]),
 A("cardinal-tetra","Cardinal Tetra","Paracheirodon axelrodi","fish","Characidae","Rio Negro region, South America","2 in",(73,81),(5.5,7.5),15,"Peaceful","Schooling, keep 6+","Mid","Intermediate","Omnivore: micro pellets, flakes, frozen foods","3-5 years",
   "Larger and more brilliantly colored than a neon, with a red stripe along the whole belly. Likes warm, clean, slightly soft water and a planted tank with some shade.",
   ["Prefers warmer water than neons (upper 70s).","Dim lighting and floating plants make them bolder.","Feed small amounts; they are shy at feeding time."],aka=["cardinals"]),
 A("ember-tetra","Ember Tetra","Hyphessobrycon amandae","fish","Characidae","Araguaia basin, Brazil","0.8 in",(73,82),(5.5,7.5),5,"Peaceful","Schooling, keep 8+","Mid","Beginner","Micro pellets, crushed flakes, baby brine shrimp","2-3 years",
   "A tiny, glowing orange tetra that is ideal for nano planted tanks. Because of its size, tankmates need to be gentle and small-mouthed.",
   ["Great with shrimp and other nano fish.","Feed tiny foods they can actually swallow.","Choose a tight-fitting lid; they can jump."],aka=["embers"]),
 A("black-skirt-tetra","Black Skirt Tetra","Gymnocorymbus ternetzi","fish","Characidae","Paraguay and Parana basins, South America","2.5 in",(70,80),(6.0,7.5),20,"Peaceful, may nip long fins","Schooling, keep 6+","Mid","Beginner","Omnivore: flakes, pellets, frozen foods","3-5 years",
   "A hardy, active tetra that tolerates a wide range of conditions. Keep it in a group to reduce fin-nipping, and avoid pairing it with long-finned fish like bettas or angelfish.",
   ["A larger group spreads out any nipping.","Skip slow, long-finned tankmates."],aka=["black skirts","blackskirt tetra"]),
 A("lemon-tetra","Lemon Tetra","Hyphessobrycon pulchripinnis","fish","Characidae","Amazon basin, Brazil","2 in",(72,82),(5.5,7.5),15,"Peaceful","Schooling, keep 6+","Mid","Beginner","Omnivore: flakes, micro pellets, frozen foods","3-5 years",
   "A soft yellow tetra with a bright red eye. Easy to keep and good in community tanks with similar-sized fish.",
   ["Looks best in a group in a planted tank.","Stable water matters more than exact numbers."],aka=["lemon tetras"]),
 A("rummy-nose-tetra","Rummy Nose Tetra","Hemigrammus rhodostomus","fish","Characidae","Amazon basin, South America","2 in",(75,82),(5.0,7.0),20,"Peaceful","Schooling, keep 8+","Mid","Intermediate","Omnivore: micro pellets, flakes, frozen foods","4-6 years",
   "A tight-schooling tetra that is a classic indicator of water quality: a pale red nose means something is off. Likes warm, very clean water.",
   ["Keep 8 or more; they school tightly.","Do frequent small water changes.","Add only to a mature, stable tank."],aka=["rummynose","rummy nose"]),
 A("congo-tetra","Congo Tetra","Phenacogrammus interruptus","fish","Alestidae","Congo basin, Africa","3.5 in",(73,82),(6.0,7.5),29,"Peaceful","Schooling, keep 6+","Mid","Intermediate","Omnivore: flakes, pellets, frozen foods","3-5 years",
   "A larger, shimmering tetra whose fins lengthen as males mature. Needs open swimming room and a gentle current.",
   ["Needs a longer tank for swimming.","Slow, long-finned fish may get harassed.","Keep a group of six or more."],aka=["congo tetras"]),
 # ---------------- Rasboras, danios, barbs, minnows ----------------
 A("harlequin-rasbora","Harlequin Rasbora","Trigonostigma heteromorpha","fish","Danionidae","Southeast Asia","2 in",(72,81),(6.0,7.5),10,"Peaceful","Schooling, keep 6+","Mid","Beginner","Omnivore: flakes, micro pellets, frozen foods","3-5 years",
   "A calm, copper-colored school fish with a black triangle. One of the most reliable community fish for planted tanks.",
   ["Keep a group of six or more.","Do well with small peaceful tankmates and shrimp."],aka=["harlequin rasboras"]),
 A("chili-rasbora","Chili Rasbora","Boraras brigittae","fish","Danionidae","Borneo","0.7 in",(73,82),(5.0,7.0),5,"Peaceful","Schooling, keep 8+","Mid to upper","Intermediate","Micro foods: crushed flakes, baby brine shrimp","2-4 years",
   "A tiny, deep-red nano fish that needs a calm, planted tank and equally gentle tankmates. Shy at first, bolder in a larger group.",
   ["Pair with other nano fish and shrimp.","Offer food small enough to swallow.","Tight lid; small fish still jump."],aka=["mosquito rasbora","chili rasboras"]),
 A("celestial-pearl-danio","Celestial Pearl Danio","Danio margaritatus","fish","Danionidae","Myanmar","1 in",(73,79),(6.5,7.5),10,"Peaceful","Groups, keep 6+","Mid to upper","Beginner","Micro pellets, flakes, frozen foods","3-5 years",
   "Also called the galaxy rasbora. Males show spangled orange fins and females are plumper and paler. Peaceful and small, but shy until they feel secure.",
   ["Plants and floating cover help them settle in.","Keep a group with a good mix of males and females."],aka=["CPD","galaxy rasbora","galaxy rasboras"]),
 A("zebra-danio","Zebra Danio","Danio rerio","fish","Danionidae","India and surrounding regions","2 in",(64,77),(6.5,7.5),10,"Peaceful, very active","Schooling, keep 6+","Upper to mid","Beginner","Omnivore: flakes, pellets, frozen foods","3-5 years",
   "A fast, hardy school fish that tolerates cooler water. Great for cycling-friendly community tanks, but too busy for very shy or slow tankmates.",
   ["Keep 6 or more.","Not the best match for long-finned bettas or slow fish.","Needs a tight lid."],aka=["zebra danios","zebrafish"]),
 A("white-cloud-mountain-minnow","White Cloud Mountain Minnow","Tanichthys albonubes","fish","Danionidae","Southern China","1.5 in",(60,75),(6.5,7.5),10,"Peaceful","Schooling, keep 6+","Upper to mid","Beginner","Flakes, micro pellets, frozen foods","3-5 years",
   "A cool-water school fish that is happy without a heater in most homes. A good choice for unheated tanks and for pairing with hardy, cooler-water species.",
   ["Tolerates cooler room temperatures.","Best in groups of six or more."],aka=["white clouds","white cloud"]),
 A("cherry-barb","Cherry Barb","Puntius titteya","fish","Cyprinidae","Sri Lanka","2 in",(73,81),(6.0,7.5),20,"Peaceful","Groups, keep 6+","Mid","Beginner","Omnivore: flakes, pellets, frozen foods","4-6 years",
   "A gentle, red barb that is far calmer than other barbs. Males color up when they have females and cover to display around.",
   ["Keep more females than males.","Dense planting makes them bolder."],aka=["cherry barbs"]),
 A("tiger-barb","Tiger Barb","Puntigrus tetrazona","fish","Cyprinidae","Sumatra and Borneo","3 in",(72,79),(6.0,7.5),20,"Semi-aggressive, fin-nipper","Schooling, keep 8+","Mid","Beginner","Omnivore: flakes, pellets, frozen foods","5-7 years",
   "Active and bold, with a reputation for nipping. Large groups spread out the aggression, and they should not be kept with long-finned or slow fish.",
   ["Keep at least 8 so they pick on each other, not tankmates.","Avoid bettas, angelfish and gouramis."],aka=["tiger barbs"]),
 A("boesemani-rainbowfish","Boesemani Rainbowfish","Melanotaenia boesemani","fish","Melanotaeniidae","Western New Guinea","4.5 in",(75,81),(7.0,8.0),40,"Peaceful, active","Schooling, keep 6+","Upper to mid","Beginner","Omnivore: flakes, pellets, frozen foods","5-8 years",
   "A colorful, active schooling fish that colors up slowly over the first year. Likes hard, alkaline water, which suits San Diego tap water well.",
   ["Needs swimming room: a longer tank.","Color develops with age and good care."],aka=["boesemani","boesemani rainbow"]),
 # ---------------- Livebearers ----------------
 A("guppy","Guppy","Poecilia reticulata","fish","Poeciliidae","Northern South America and Caribbean","1.5 in (male) to 2.5 in (female)",(72,82),(7.0,8.0),10,"Peaceful","Groups; more females than males","Upper to mid","Beginner","Omnivore: flakes, micro pellets, frozen foods","2-3 years",
   "Hardy, colorful livebearers that breed readily. Keep more females than males to reduce harassment, and plan for fry.",
   ["Two or three females per male.","They breed fast; be ready for babies.","Like hard, alkaline water."],aka=["guppies","fancy guppy"]),
 A("endlers-livebearer","Endler's Livebearer","Poecilia wingei","fish","Poeciliidae","Venezuela","1 in (male) to 1.8 in (female)",(72,82),(7.0,8.0),10,"Peaceful","Groups; more females than males","Upper to mid","Beginner","Omnivore: flakes, micro pellets","2-3 years",
   "A small, vivid relative of the guppy. A bit more nano-friendly, but equally prolific.",
   ["Keep more females than males.","Will interbreed with guppies."],aka=["endlers","endler","endler's"]),
 A("platy","Platy","Xiphophorus maculatus","fish","Poeciliidae","Mexico and Central America","2.5 in",(70,80),(7.0,8.2),15,"Peaceful","Groups; more females than males","Mid","Beginner","Omnivore: flakes, pellets, veggie foods","3-4 years",
   "A cheerful, easy livebearer in many colors. Good for new keepers who have hard water.",
   ["Keep more females than males.","Add some vegetable-based food."],aka=["platies","mickey mouse platy"]),
 A("molly","Molly","Poecilia sphenops","fish","Poeciliidae","Central America and Mexico","4 in",(72,82),(7.5,8.5),20,"Peaceful","Groups; more females than males","Mid to upper","Beginner","Omnivore: flakes, algae, veggie foods","3-5 years",
   "A hardy livebearer that likes hard, alkaline water and a little vegetable matter in its diet. Some keepers add a little aquarium salt, but it is not required for most freshwater tanks.",
   ["Needs hard, alkaline water.","Offer algae wafers or blanched veggies."],aka=["mollies","black molly","dalmatian molly"]),
 A("swordtail","Swordtail","Xiphophorus hellerii","fish","Poeciliidae","Mexico and Central America","4-5 in",(70,82),(7.0,8.4),29,"Peaceful; males can squabble","Groups; more females than males","Mid to upper","Beginner","Omnivore: flakes, pellets, veggie foods","3-5 years",
   "An active livebearer named for the male's sword-like tail extension. Needs a longer tank and a tight lid.",
   ["Keep one male with several females.","Needs a tight lid; they jump."],aka=["swordtails"]),
 # ---------------- Bottom dwellers & algae eaters ----------------
 A("panda-corydoras","Panda Cory","Corydoras panda","fish","Callichthyidae","Peru","2 in",(68,77),(6.0,7.5),15,"Peaceful","Groups, keep 6+","Bottom","Beginner","Sinking pellets, wafers, frozen foods","4-5 years",
   "A small, black-and-white armored catfish that likes soft sand and company. Prefers slightly cooler water than many tropical fish.",
   ["Use sand or smooth gravel to protect their barbels.","Keep 6 or more.","Make sure sinking food reaches them."],aka=["panda cory","panda corys","panda catfish"]),
 A("bronze-corydoras","Bronze Cory","Corydoras aeneus","fish","Callichthyidae","South America","2.5 in",(72,79),(6.0,8.0),20,"Peaceful","Groups, keep 6+","Bottom","Beginner","Sinking pellets, wafers, frozen foods","5-10 years",
   "A hardy, long-lived cory that tolerates a wide range of water. A reliable clean-up crew member for community tanks.",
   ["Keep 6 or more.","Feed sinking foods after lights dim."],aka=["bronze cory","bronze corys","aeneus cory","albino cory","albino corys"]),
 A("kuhli-loach","Kuhli Loach","Pangio kuhlii","fish","Cobitidae","Southeast Asia","4 in",(75,86),(6.0,7.0),20,"Peaceful, shy","Groups, keep 5+","Bottom","Intermediate","Sinking pellets, frozen and live foods","10+ years",
   "An eel-like, nocturnal loach that hides in plants and leaf litter. Needs soft sand and plenty of cover, and a tightly covered tank because they escape through tiny gaps.",
   ["Use sand, not sharp gravel.","Cover every gap; they escape.","Feed after lights out."],aka=["kuhli loaches","kuhlii"]),
 A("clown-loach","Clown Loach","Chromobotia macracanthus","fish","Botiidae","Sumatra and Borneo","8-12 in",(75,86),(6.0,7.5),125,"Peaceful but boisterous","Groups, keep 5+","Bottom","Intermediate","Omnivore: sinking pellets, frozen foods, snails","15-25 years",
   "A famous, long-lived loach that gets much larger than the juveniles sold. Needs a big tank and a group, and can be sensitive to ich.",
   ["Plan for a very large tank at full size.","Quarantine new fish; they are ich-prone.","Provide caves and wood."],aka=["clown loaches"]),
 A("bristlenose-pleco","Bristlenose Pleco","Ancistrus sp.","fish","Loricariidae","South America","4-5 in",(73,81),(6.5,7.5),25,"Peaceful","Solitary; one per tank","Bottom","Beginner","Algae, sinking wafers, blanched veggies, driftwood","5-10 years",
   "The small, practical pleco. Stays far smaller than common plecos and munches algae and biofilm. Needs driftwood to graze on.",
   ["Always keep driftwood in the tank.","Males can be territorial with each other.","Supplement with veggie wafers."],aka=["bristlenose","bushynose pleco","bristle nose pleco","bn pleco"]),
 A("otocinclus","Otocinclus","Otocinclus sp.","fish","Loricariidae","South America","1.5-2 in",(72,79),(6.5,7.5),15,"Peaceful","Groups, keep 4+","Mid to bottom (on plants and glass)","Intermediate","Algae and biofilm; supplement with veggie wafers","3-5 years",
   "A tiny algae-grazing catfish that does best in a mature, planted tank with a steady supply of biofilm. Often fragile when newly imported.",
   ["Add only to a tank with visible algae or biofilm.","Supplement with veggie foods.","Keep a group of 4 or more."],aka=["oto","otos","oto cat","otocinclus catfish"]),
 A("siamese-algae-eater","Siamese Algae Eater","Crossocheilus oblongus","fish","Cyprinidae","Southeast Asia","5-6 in",(75,79),(6.5,7.5),30,"Peaceful, can chase its own kind","Single or small group","Bottom to mid","Intermediate","Algae, flakes, pellets, veggies","8-10 years",
   "A busy grazer that eats some types of algae. Active and fast, and best in a longer tank with current. Be careful to buy the true species, not look-alikes.",
   ["Needs a longer tank with some current.","Provide wood and plants for grazing."],aka=["SAE","siamese algae eaters"]),
 # ---------------- Labyrinth fish ----------------
 A("betta","Betta","Betta splendens","fish","Osphronemidae","Thailand and Southeast Asia","2.5-3 in",(76,82),(6.5,7.5),5,"Aggressive toward other bettas","Solitary","Top","Beginner","Carnivore: betta pellets, frozen foods","3-5 years",
   "A bold, long-finned labyrinth fish that breathes air at the surface. Males cannot share a tank with one another. Needs a heated, filtered tank, not a bowl.",
   ["Heater and gentle filter, not a bowl.","Never house two males together.","Avoid fin-nipping tankmates."],aka=["bettas","betta fish","siamese fighting fish"]),
 A("dwarf-gourami","Dwarf Gourami","Trichogaster lalius","fish","Osphronemidae","India and Bangladesh","3 in",(74,82),(6.0,7.5),20,"Peaceful; males can squabble","Solitary or pairs","Top to mid","Intermediate","Omnivore: flakes, pellets, frozen foods","4-6 years",
   "A colorful, calm gourami that is prone to a viral disease in commercial stock. Choose healthy fish and quarantine carefully.",
   ["Buy only active, clear-finned fish.","Quarantine new arrivals.","One male per tank unless it is large and well planted."],aka=["dwarf gouramis","powder blue gourami","neon blue gourami"]),
 A("honey-gourami","Honey Gourami","Trichogaster chuna","fish","Osphronemidae","India and Bangladesh","2 in",(72,82),(6.0,7.5),10,"Peaceful","Solitary or pairs","Top to mid","Beginner","Omnivore: flakes, micro pellets, frozen foods","4-8 years",
   "A small, mellow gourami that is hardier than dwarfs. A good centerpiece for a peaceful nano tank with floating plants.",
   ["Floating plants help them feel safe.","Great with other small, calm fish."],aka=["honey gouramis"]),
 A("pearl-gourami","Pearl Gourami","Trichopodus leerii","fish","Osphronemidae","Southeast Asia","4-5 in",(77,82),(6.0,8.0),30,"Peaceful","Pair or solitary","Top to mid","Beginner","Omnivore: flakes, pellets, frozen foods","4-8 years",
   "An elegant, gentle gourami with a lace-like pattern. Likes a planted tank with floating plants and calm tankmates.",
   ["Floating plants make them more confident.","Avoid boisterous fin-nippers."],aka=["pearl gouramis","lace gourami"]),
 A("blue-gourami","Blue Gourami (Three Spot)","Trichopodus trichopterus","fish","Osphronemidae","Southeast Asia","5-6 in",(72,82),(6.0,8.0),30,"Semi-aggressive","Solitary or pair","Top to mid","Beginner","Omnivore: flakes, pellets, frozen foods","4-6 years",
   "A big, hardy gourami that can be pushy with smaller or similar-shaped fish. Better in a larger, well-planted tank.",
   ["Males can be aggressive with each other.","Needs a larger tank than small gouramis."],aka=["three spot gourami","opaline gourami","gold gourami"]),
 # ---------------- Cichlids ----------------
 A("german-blue-ram","German Blue Ram","Mikrogeophagus ramirezi","fish","Cichlidae","Venezuela and Colombia","2-2.8 in",(78,84),(5.5,7.0),20,"Peaceful","Pair","Bottom to mid","Intermediate","Micro pellets, frozen and live foods","2-4 years",
   "A jewel-like dwarf cichlid that likes warm, clean, soft-to-moderate water. Delicate compared with most community fish, so buy healthy stock and keep conditions steady.",
   ["Needs warm, very stable water.","Buy tank-raised, healthy fish.","Provide caves and smooth sand."],aka=["blue ram","ram cichlid","rams","gold ram"]),
 A("bolivian-ram","Bolivian Ram","Mikrogeophagus altispinosus","fish","Cichlidae","Bolivia and Brazil","3 in",(72,80),(6.0,7.5),20,"Peaceful","Pair","Bottom to mid","Beginner","Micro pellets, frozen foods","3-4 years",
   "A hardier, larger cousin of the German blue ram that tolerates cooler water and wider conditions.",
   ["Better first dwarf cichlid than the German ram.","Provide smooth sand and caves."],aka=["bolivian rams"]),
 A("cockatoo-apistogramma","Cockatoo Apistogramma","Apistogramma cacatuoides","fish","Cichlidae","Peru and Brazil","2-3.5 in",(73,82),(6.0,7.5),20,"Peaceful for a cichlid; territorial","One male with 2-3 females","Bottom to mid","Intermediate","Micro pellets, frozen and live foods","3-5 years",
   "A colorful, easier dwarf cichlid. Males set up territories and need caves and line-of-sight breaks. See our dedicated Apistogramma guide at apistogrammarama.com.",
   ["Provide a cave per female.","Keep one male per tank unless it is large.","Use leaf litter, caves, plants."],aka=["cockatoo dwarf cichlid","apisto","apistogramma"]),
 A("angelfish","Angelfish","Pterophyllum scalare","fish","Cichlidae","Amazon basin, South America","6 in long, 10 in tall",(76,84),(6.0,7.5),55,"Semi-aggressive; will eat tiny fish","Pair or small group","Mid to upper","Intermediate","Omnivore: flakes, pellets, frozen foods","8-10 years",
   "A tall, elegant cichlid that needs a tall tank. Small tetras like neons can end up as food once the angelfish is grown.",
   ["Needs a tall tank.","Avoid tiny schooling fish like neons.","Avoid fin-nipping tankmates."],aka=["angelfish","angel fish","koi angelfish"]),
 A("discus","Discus","Symphysodon aequifasciatus","fish","Cichlidae","Amazon basin, South America","6-8 in",(82,86),(6.0,7.0),75,"Peaceful but shy","Groups, keep 5+","Mid","Advanced","Discus pellets, frozen and live foods","10-15 years",
   "The 'king of the aquarium': a disc-shaped, warm-water cichlid that demands pristine water, high temperatures and frequent water changes. See our Discus Guides site for in-depth care.",
   ["Needs very warm, very clean water.","Large, frequent water changes.","Feed several small meals, not one big one."],aka=["discus fish","pigeon blood discus"]),
 A("oscar","Oscar","Astronotus ocellatus","fish","Cichlidae","Amazon basin, South America","12-14 in",(74,81),(6.0,8.0),75,"Aggressive and predatory","Solitary or large mated pair","All levels","Intermediate","Carnivore: pellets, frozen foods","10-15 years",
   "An intelligent, big, messy cichlid with a lot of personality. Needs a large tank and powerful filtration, and any fish that fits in its mouth will be eaten.",
   ["Heavy bioload: oversize the filter.","Rearranges decor; secure heavy items.","Tank mates must be large and tough."],aka=["oscars","tiger oscar","red oscar"]),
 A("convict-cichlid","Convict Cichlid","Amatitlania nigrofasciata","fish","Cichlidae","Central America","4-5 in",(74,79),(6.5,8.0),30,"Aggressive, especially when breeding","Pair","Bottom to mid","Beginner","Omnivore: pellets, frozen foods","8-10 years",
   "A hardy, prolific, feisty cichlid. A great first cichlid for a species tank, but tankmates will be bullied when it breeds.",
   ["Best kept in a pair, alone or with large tough fish.","Provide caves.","Breeds easily."],aka=["convicts","zebra cichlid"]),
 A("electric-yellow-lab","Electric Yellow Lab","Labidochromis caeruleus","fish","Cichlidae","Lake Malawi, Africa","4 in",(76,82),(7.8,8.6),30,"Semi-aggressive (mild for a mbuna)","One male with several females","Mid to bottom","Beginner","Omnivore: cichlid pellets and veggie foods","6-10 years",
   "A bright yellow Lake Malawi mbuna and one of the gentler ones. Needs hard, alkaline water and rockwork, and does best with other Malawi cichlids.",
   ["Needs hard, alkaline water.","Stack rocks for caves, with sturdy placement.","Keep other Malawi fish, not tropical community fish."],aka=["yellow lab","electric yellow","electric yellows","yellow labs"]),
 A("kribensis","Kribensis","Pelvicachromis pulcher","fish","Cichlidae","West Africa","3-4 in",(73,82),(6.0,7.5),20,"Semi-aggressive when breeding","Pair","Bottom","Beginner","Omnivore: pellets, frozen foods","5 years",
   "A small, colorful West African cichlid that is a classic cave-breeder and fiercely protective parent. Gets along with larger peaceful community fish.",
   ["Provide caves such as half coconut shells.","Pairs defend the cave when breeding."],aka=["krib","kribs","rainbow krib"]),
 A("jack-dempsey","Jack Dempsey","Rocio octofasciata","fish","Cichlidae","Central America","8-10 in",(75,82),(7.0,8.0),75,"Aggressive","Solitary or pair","All levels","Intermediate","Carnivore: pellets, frozen foods","10-15 years",
   "A hardy, blue-speckled Central American cichlid with a big attitude. Needs a large tank and strong filtration, and tankmates must be large and tough.",
   ["Oversize the filter.","Tankmates must be big and robust.","Rearranges decor."],aka=["jack dempsey cichlid","jd"]),
 A("flowerhorn","Flowerhorn Cichlid","Hybrid (Amphilophus x Vieja/Paraneetroplus lines)","fish","Cichlidae","Captive-bred hybrid","10-12 in",(78,84),(7.0,8.0),75,"Aggressive","Solitary","All levels","Intermediate","Carnivore: quality cichlid pellets, occasional frozen foods","10-12 years",
   "A captive-bred hybrid known for its bold colors and prominent head hump. Intelligent, interactive and territorial: it needs its own large, well-filtered tank. See our dedicated Flowerhorn Hobby site.",
   ["Keep alone.","Heavy bioload: strong filtration and big water changes.","Choose a sturdy glass or acrylic with a lid."],aka=["flowerhorn","flower horn","fh"]),
 # ---------------- Specialty ----------------
 A("pea-puffer","Pea Puffer","Carinotetraodon travancoricus","fish","Tetraodontidae","Southwest India","1-1.4 in",(74,82),(6.8,7.8),5,"Semi-aggressive","Solitary in 5 gal; groups in 15+ gal with lots of plants","Mid","Intermediate","Carnivore: live and frozen foods; snails help wear their beak","4-5 years",
   "The smallest puffer. Personable but nippy and a picky carnivore that needs snails, frozen foods and sometimes live foods.",
   ["Needs live or frozen foods; no flakes.","Do not keep with fin-nipping-vulnerable tankmates.","Add plenty of plants for line of sight breaks."],aka=["pea puffers","dwarf puffer","dwarf puffers"]),
 A("figure-8-puffer","Figure 8 Puffer","Dichotomyctere biocellatus","fish","Tetraodontidae","Southeast Asia (brackish estuaries)","3 in",(74,82),(7.5,8.5),20,"Aggressive","Solitary","Mid","Advanced","Carnivore: snails, shrimp, frozen foods","~10 years",
   "A small, brackish puffer that needs salinity (specific gravity about 1.005-1.008) to stay healthy, plus a diet of hard-shelled foods to wear down its beak.",
   ["Needs brackish water; do not keep in plain freshwater long-term.","Feed snails and shell-on foods.","Keep alone."],aka=["figure eight puffer","f8 puffer","figure 8 puffers"]),
 A("fancy-goldfish","Fancy Goldfish","Carassius auratus","fish","Cyprinidae","Cultivated in East Asia","6-8 in",(65,75),(6.5,8.0),30,"Peaceful","Groups","All levels","Beginner","Omnivore: sinking goldfish pellets, veggies","10-15+ years",
   "Round-bodied goldfish such as orandas, ranchus and fantails. Heavy waste producers that need big tanks and strong filtration, not bowls. See our goldfish vs. tropical fish guide for why they can't share with tropicals.",
   ["Plan 30 gallons for the first fish plus 10-20 for each additional.","Strong filtration and weekly water changes.","Do not mix with tropical fish."],aka=["goldfish","oranda","ranchu","fantail goldfish","lionhead goldfish"]),
 A("comet-goldfish","Comet Goldfish","Carassius auratus","fish","Cyprinidae","Cultivated in East Asia","10-12 in",(60,75),(6.5,8.0),75,"Peaceful, very active","Groups","All levels","Beginner","Omnivore: goldfish pellets, veggies","10-20 years",
   "The classic long-bodied, single-tailed goldfish. Active and large, and best suited to a pond or a very large tank.",
   ["Needs a pond or very large tank.","Heavy waste: strong filtration.","Do not keep with tropical fish."],aka=["comets","feeder goldfish","common goldfish"]),
 A("silver-arowana","Silver Arowana","Osteoglossum bicirrhosum","fish","Osteoglossidae","Amazon basin, South America","30-36 in",(75,86),(6.0,7.0),250,"Aggressive and predatory","Solitary","Top","Advanced","Carnivore: pellets, frozen fish and insects","10-15+ years",
   "A giant surface-dwelling predator that can jump straight through gaps in a lid. Needs a very large tank with a heavy, secure cover, and it will eat anything it can swallow.",
   ["Secure, heavy lid; they jump.","Needs a very large tank as an adult.","Tankmates must be large enough not to be eaten."],aka=["silver arowanas","arowana","arowanas"]),
 # ---------------- Inverts ----------------
 A("neocaridina-shrimp","Neocaridina Shrimp","Neocaridina davidi","invert","Atyidae","Taiwan and China (captive-bred colors)","1-1.5 in",(65,80),(6.5,8.0),5,"Peaceful","Colony, start with 6+","Bottom","Beginner","Biofilm, algae, shrimp pellets, blanched veggies","1-2 years",
   "Cherry shrimp and other color morphs. Easy, active and breed readily in a planted tank, but sensitive to copper and some medications.",
   ["Never use copper-based medications.","Add after the tank has cycled.","Acclimate slowly, with drip acclimation."],aka=["cherry shrimp","red cherry shrimp","blue dream shrimp","neocaridina","rili shrimp"]),
 A("amano-shrimp","Amano Shrimp","Caridina multidentata","invert","Atyidae","Japan and Taiwan","2 in",(70,78),(6.5,7.5),10,"Peaceful","Groups","All levels","Beginner","Algae, biofilm, shrimp pellets, blanched veggies","2-3 years",
   "A larger, tireless algae grazer. They breed only in brackish water, so they will not overrun a freshwater tank.",
   ["Acclimate slowly.","Great algae eaters.","Secure the lid; they can climb out."],aka=["amano shrimps","amano"]),
 A("nerite-snail","Nerite Snail","Neritina sp.","invert","Neritidae","Africa and Indo-Pacific","1 in",(72,78),(7.0,8.5),5,"Peaceful","Solitary or groups","All levels","Beginner","Algae and biofilm","1-2 years",
   "A hard-working algae-eating snail that will not overrun a tank because its eggs rarely hatch in freshwater. Needs hard water with some calcium to keep its shell healthy, and a lid, because it climbs.",
   ["Needs hard water for shell health.","Will leave small white eggs on hardscape.","Needs a secure lid."],aka=["nerite snails","zebra nerite","tiger nerite"]),
 A("mystery-snail","Mystery Snail","Pomacea diffusa / bridgesii","invert","Ampullariidae","South America","2 in",(68,82),(7.0,8.0),5,"Peaceful","Solitary or groups","All levels","Beginner","Algae, veggies, sinking pellets","1-3 years",
   "A big, charismatic scavenger that breathes air at the surface and lays eggs above the waterline. Keep a gap at the top of the tank. It can also nibble delicate plants if underfed.",
   ["Leave air space at the top.","Needs calcium in the water for shell health.","Feed veggies so plants are left alone."],aka=["mystery snails","apple snail","golden mystery snail"]),
]

PLANTS = [
 P("java-fern","Java Fern","Microsorum pteropus","Polypodiaceae","Southeast Asia","6-14 in","Low","Not required","Attach to wood or rock","Slow","68-82°F","6.0-7.5","Beginner","Rhizome division, plantlets on old leaves",
   "A tough, shade-tolerant fern that grows attached to wood or rock. Do not bury the rhizome, or it will rot.",
   ["Tie or glue onto hardscape; do not plant in substrate.","Black spots on old leaves are normal.","Thrives in low light, great for beginners."],aka=["java ferns"]),
 P("anubias-nana","Anubias Nana","Anubias barteri var. nana","Araceae","West Africa","4-6 in","Low to moderate","Not required","Attach to wood or rock","Very slow","72-82°F","6.0-7.5","Beginner","Rhizome division",
   "An exceptionally hardy, slow-growing plant with broad dark leaves. Keep the rhizome above the substrate, and keep algae off its slow leaves with lower light.",
   ["Never bury the rhizome.","Lower light keeps algae off the leaves.","Good for fish that dig or nibble."],aka=["anubias","anubias nana petite","nana petite"]),
 P("java-moss","Java Moss","Taxiphyllum barbieri","Hypnaceae","Southeast Asia","2-4 in","Low to moderate","Not required","Attach to wood, rock or mesh","Moderate","68-82°F","6.0-7.5","Beginner","Cuttings",
   "A forgiving moss used for shrimp cover, fry cover and carpets. Trim regularly so it doesn't become a tangle.",
   ["Tie to wood or rock with thread.","Great cover for shrimp and fry.","Trim to keep it neat and clean."],aka=["moss"]),
 P("amazon-sword","Amazon Sword","Echinodorus bleheri","Alismataceae","South America","12-20 in","Moderate","Not required","Background","Moderate","72-82°F","6.5-7.5","Beginner","Runners and adventitious plantlets",
   "A big, classic centerpiece plant. A heavy root feeder, so give it a nutrient-rich substrate or root tabs.",
   ["Use root tabs or rich substrate.","Needs room to grow upward.","Old leaves yellow and can be trimmed."],aka=["sword plant","amazon sword plant","echinodorus"]),
 P("vallisneria","Vallisneria","Vallisneria spiralis","Hydrocharitaceae","Worldwide tropics and subtropics","12-24+ in","Low to moderate","Not required","Background","Fast","65-82°F","6.5-8.0","Beginner","Runners",
   "A tall, grass-like plant that spreads by runners and tolerates hard, alkaline water well, which suits San Diego tap water.",
   ["Plant in substrate, not the crown.","Spreads by runners; thin as needed.","Good for hard-water tanks."],aka=["val","jungle val","straight val"]),
 P("cryptocoryne-wendtii","Cryptocoryne Wendtii","Cryptocoryne wendtii","Araceae","Sri Lanka","4-8 in","Low to moderate","Not required","Midground","Slow to moderate","72-82°F","6.0-7.5","Beginner","Runners",
   "A hardy, low-light rosette plant that comes in many colors. May 'melt' when moved, then regrow from the roots.",
   ["Do not panic if leaves melt after planting.","Root tabs help it spread.","Leave it alone once settled."],aka=["crypt","cryptocoryne","crypt wendtii"]),
 P("water-wisteria","Water Wisteria","Hygrophila difformis","Acanthaceae","South and Southeast Asia","12-20 in","Moderate","Not required","Midground to background","Fast","72-82°F","6.5-7.5","Beginner","Stem cuttings",
   "A fast-growing, easy stem plant with lace-like or broad leaves depending on light. Good for soaking up excess nutrients.",
   ["Trim and replant tops.","Bright light gives bushier growth."],aka=["wisteria","hygrophila"]),
 P("ludwigia-repens","Ludwigia Repens","Ludwigia repens","Onagraceae","North and Central America","8-16 in","Moderate to high","Helpful","Midground to background","Moderate","68-82°F","6.0-7.5","Beginner","Stem cuttings",
   "A sturdy stem plant that turns red under strong light. Easy and fast-growing, and a great starter stem plant.",
   ["Higher light brings out red tones.","Trim and replant the tops."],aka=["ludwigia","red ludwigia"]),
 P("rotala-rotundifolia","Rotala Rotundifolia","Rotala rotundifolia","Lythraceae","Asia","6-12+ in","Moderate to high","Helpful","Midground to background","Moderate to fast","72-82°F","6.0-7.0","Intermediate","Stem cuttings",
   "A fine-leaved stem plant that turns pink-orange in strong light. Responds well to CO2 and regular fertilizing.",
   ["Needs steady fertilizers and light.","Trim often for dense bushes."],aka=["rotala","rotala indica"]),
 P("bucephalandra","Bucephalandra","Bucephalandra sp.","Araceae","Borneo","2-6 in","Low to moderate","Not required","Attach to wood or rock","Very slow","72-82°F","6.0-7.5","Intermediate","Rhizome division",
   "A slow, jewel-like epiphyte with iridescent leaves, used to detail hardscape. Attach to rock or wood and keep the rhizome clear of the substrate.",
   ["Attach to hardscape.","Keep water stable; they are slow to adapt.","Do not bury the rhizome."],aka=["bucce","buce","bucephalandra"]),
 P("monte-carlo","Monte Carlo","Micranthemum tweediei","Linderniaceae","South America","1-2 in","High","Recommended","Foreground carpet","Moderate","68-78°F","6.0-7.5","Intermediate","Division, trimming",
   "A low carpeting plant that makes a lush lawn under strong light and CO2. Needs bright light and a nutrient-rich substrate to stay compact.",
   ["Plant in small clumps.","Needs strong light, CO2 and fertilizing.","Trim regularly to keep it dense."],aka=["mc","monte carlo carpet"]),
 P("dwarf-hairgrass","Dwarf Hairgrass","Eleocharis acicularis","Cyperaceae","Worldwide","2-6 in","Moderate to high","Recommended","Foreground carpet","Moderate","68-82°F","6.0-7.5","Intermediate","Runners",
   "A fine, grass-like carpet plant that spreads by runners. Needs bright light and trimming to stay low.",
   ["Plant in small tufts.","Trim to keep it low.","Needs light, nutrients and patience."],aka=["hairgrass","dwarf hair grass","eleocharis"]),
 P("anacharis","Anacharis (Egeria)","Egeria densa","Hydrocharitaceae","South America","12-24+ in","Moderate","Not required","Background or floating","Very fast","60-82°F","6.0-8.0","Beginner","Stem cuttings",
   "A fast, cool-tolerant stem plant that absorbs nutrients quickly and helps keep algae in check. Also good for goldfish tanks, as it is cool-water tolerant (but goldfish may nibble it).",
   ["Trim often; it grows fast.","Cool-water tolerant.","Float or plant in substrate."],aka=["elodea","egeria","anacharis"]),
 P("amazon-frogbit","Amazon Frogbit","Limnobium laevigatum","Hydrocharitaceae","Central and South America","Floating; roots 6+ in","Moderate to high","Not required","Floating","Fast","68-86°F","6.0-8.0","Beginner","Runners",
   "A floating plant with trailing roots. Gives shade, cover for shy fish, and absorbs nutrients. Keep the leaves dry; they rot if constantly wet from a filter outlet.",
   ["Keep the leaves dry from splashing.","Thin as needed.","Great for betta and shy fish tanks."],aka=["frogbit","floating plant"]),
]

try:
    import care_data2 as _d2
    ANIMALS = ANIMALS + _d2.MORE_ANIMALS
    PLANTS = PLANTS + _d2.MORE_PLANTS
except ImportError:
    _d2 = None
try:
    import care_data3 as _d3
    ANIMALS = ANIMALS + _d3.MORE_ANIMALS
    PLANTS = PLANTS + _d3.MORE_PLANTS
except ImportError:
    _d3 = None
ALL = ANIMALS + PLANTS
if _d2:
    _by = {e["slug"]: e for e in ALL}
    _alias = dict(_d2.ALIAS_INTO)
    if _d3:
        for _k, _v in getattr(_d3, "ALIAS_INTO", {}).items():
            _alias[_k] = list(_alias.get(_k, [])) + list(_v)
    for _s, _al in _alias.items():
        for _a in _al:
            if _a not in _by[_s]["aka"]:
                _by[_s]["aka"].append(_a)
    _names = {e["name"].lower() for e in ALL}
    for _e in ALL:
        _e["aka"] = [a for a in dict.fromkeys(_e["aka"]) if a.lower() not in _names or a.lower() == _e["name"].lower()]
    _seen = set()
    for _e in ALL:
        _keep = []
        for _a in _e["aka"]:
            if _a.lower() not in _seen:
                _seen.add(_a.lower()); _keep.append(_a)
        _e["aka"] = _keep

#!/usr/bin/env python3
def part1(ll):
    raise NotImplementedError

def part2(ll):
    raise NotImplementedError

TEST_INPUT = """--- scanner 0 ---
404,-588,-901
528,-643,409
-838,591,734
390,-675,-793
-537,-823,-458
-485,-357,347
-345,-311,381
-661,-816,-575
-876,649,763
-618,-824,-621
553,345,-567
474,580,667
-447,-329,318
-584,868,-557
544,-627,-890
564,392,-477
455,729,728
-892,524,684
-689,845,-530
423,-701,434
7,-33,-71
630,319,-379
443,580,662
-789,900,-551
459,-707,401

--- scanner 1 ---
686,422,578
605,423,415
515,917,-361
-336,658,858
95,138,22
-476,619,847
-340,-569,-846
567,-361,727
-460,603,-452
669,-402,600
729,430,532
-500,-761,534
-322,571,750
-466,-666,-811
-429,-592,574
-355,545,-477
703,-491,-529
-328,-685,520
413,935,-424
-391,539,-444
586,-435,557
-364,-763,-893
807,-499,-711
755,-354,-619
553,889,-390

--- scanner 2 ---
649,640,665
682,-795,504
-784,533,-524
-644,584,-595
-588,-843,648
-30,6,44
-674,560,763
500,723,-460
609,671,-379
-555,-800,653
-675,-892,-343
697,-426,-610
578,704,681
493,664,-388
-671,-858,530
-667,343,800
571,-461,-707
-138,-166,112
-889,563,-600
646,-828,498
640,759,510
-630,509,768
-681,-892,-333
673,-379,-804
-742,-814,-386
577,-820,562

--- scanner 3 ---
-589,542,597
605,-692,669
-500,565,-823
-660,373,557
-458,-679,-417
-488,449,543
-626,468,-788
338,-750,-386
528,-832,-391
562,-778,733
-938,-730,414
543,643,-506
-524,371,-870
407,773,750
-104,29,83
378,-903,-323
-778,-728,485
426,699,580
-438,-605,-362
-469,-447,-387
509,732,623
647,635,-688
-868,-804,481
614,-800,639
595,780,-596

--- scanner 4 ---
727,592,562
-293,-554,779
441,611,-461
-714,465,-776
-743,427,-804
-660,-479,-426
832,-632,460
927,-485,-438
408,393,-506
466,436,-512
110,16,151
-258,-428,682
-393,719,612
-211,-452,876
808,-476,-593
-575,615,604
-485,667,467
-680,325,-822
-627,-443,-432
872,-547,-609
833,512,582
807,604,487
839,-516,451
891,-625,532
-652,-548,-490
30,-46,-14"""

TEST_SOL = [79]

FULL_INPUT = """--- scanner 0 ---
-95,47,-4
-433,339,686
776,-791,349
699,422,-931
-601,428,-786
-518,-659,-472
366,279,475
-391,306,703
-824,-591,783
671,-803,268
649,319,-908
-834,-443,814
-608,-627,-525
313,315,609
-818,-582,819
261,-812,-636
-627,388,-788
372,-879,-622
646,435,-799
-656,326,698
496,289,546
-54,-128,-110
458,-820,-572
-702,461,-876
-522,-693,-443
707,-633,286

--- scanner 1 ---
-621,648,-820
548,-689,577
666,-363,-834
-494,-719,317
619,-388,-688
-691,580,-706
561,661,-589
-805,-703,-760
864,552,430
765,611,-569
733,608,353
-579,580,591
-585,709,-667
538,-834,461
-450,516,592
-803,-693,-633
-8,-36,9
803,550,500
-564,-863,270
655,691,-604
460,-853,551
-673,-636,-666
663,-527,-739
-614,526,662
-500,-792,428
-85,66,-117

--- scanner 2 ---
506,-840,-500
-578,616,566
629,521,-331
-509,658,663
-539,-732,628
749,411,-284
358,-840,-425
724,754,565
-32,-6,28
684,615,652
-609,-486,-405
-498,-691,484
735,466,-311
-696,-506,-560
417,-447,812
443,-552,907
-383,-705,600
-742,746,-443
750,791,680
-666,-479,-438
427,-671,814
-600,587,563
-738,818,-399
496,-837,-425
-831,729,-336

--- scanner 3 ---
549,651,656
548,522,592
823,566,-643
-638,652,858
589,-388,-777
-596,918,-481
-701,-592,870
640,-731,626
712,572,-716
-370,-283,-649
-542,-675,911
92,22,96
-686,893,-505
710,-792,628
870,636,-787
-413,-270,-655
563,-476,-613
-589,949,-441
-626,-566,934
787,-661,684
-416,-418,-720
-533,722,741
478,686,602
-22,188,141
679,-466,-758
-538,593,818

--- scanner 4 ---
-552,649,769
-521,-572,-793
-626,660,740
-675,-581,497
-718,-572,427
766,782,-573
-559,-520,-784
-598,804,723
-476,662,-447
-539,660,-416
564,706,664
628,-727,-687
-562,-624,-820
-785,-523,523
859,710,-571
736,689,-604
-425,626,-467
796,-756,-594
814,-605,660
-36,2,-25
550,798,618
731,-582,801
536,570,609
721,-801,-589
797,-590,762

--- scanner 5 ---
548,-495,250
-563,-656,332
633,896,516
777,492,-501
-853,497,767
-860,-500,-474
533,-452,472
-148,176,11
605,594,-516
742,675,-555
726,771,519
713,936,526
19,46,-48
686,-464,-602
-487,566,-719
-848,405,667
552,-458,273
-158,13,-166
-588,-529,375
-928,459,611
-872,-535,-689
-567,718,-684
-749,-518,-605
697,-456,-628
-391,695,-699
569,-408,-568
-558,-466,305

--- scanner 6 ---
-725,571,493
-423,-457,336
-819,611,-536
522,627,660
540,-667,-374
530,563,-855
545,586,-679
-536,-698,-407
639,-625,579
624,-719,549
624,-650,-497
408,557,592
561,521,531
-762,624,661
-92,-137,99
-868,551,-651
-731,557,760
-539,-769,-501
-382,-362,448
-477,-667,-372
-803,440,-582
-455,-392,474
755,-632,-386
510,434,-759
659,-829,629
32,-77,-72
-140,39,-51

--- scanner 7 ---
487,589,-526
-774,-482,-623
424,409,984
694,-503,-447
-554,-575,789
796,-673,691
697,-408,-283
-657,748,659
-772,-609,-613
-660,-536,660
-477,686,-508
-590,-422,728
686,-638,771
-534,604,-408
359,441,846
421,413,-498
-604,711,827
-642,-576,-556
650,-554,-308
447,450,-613
329,368,872
592,-653,741
-79,27,50
-590,717,560
-619,680,-444

--- scanner 8 ---
-585,-677,-842
786,775,473
842,-864,447
866,714,492
87,-105,-74
652,-891,442
681,-946,-664
766,736,568
756,563,-620
734,686,-608
715,-821,472
-311,-429,737
-528,760,785
-560,801,786
-710,-680,-749
-377,380,-936
714,489,-610
-750,-670,-829
-273,-585,812
644,-923,-668
-423,384,-755
-219,-529,732
-319,398,-841
-376,752,826
638,-724,-649

--- scanner 9 ---
576,-382,-424
-492,525,-329
440,636,812
-513,-307,-637
-82,56,129
-448,401,-316
405,-290,688
490,635,714
-446,-297,-609
693,736,-397
773,692,-367
-817,636,760
-731,611,682
-617,-365,-629
31,-50,-15
-786,-449,668
699,-337,-309
-609,378,-334
705,773,-326
357,-411,635
680,-350,-544
342,-372,552
-687,585,734
-712,-464,777
-797,-631,772
333,620,822

--- scanner 10 ---
398,-470,-523
-643,-600,483
748,564,-445
-428,-635,495
-696,479,928
-559,-617,606
-463,512,-604
784,460,-448
-533,503,-561
-544,-642,-470
378,-479,792
-29,-94,163
-798,494,911
-559,561,-671
40,38,44
651,357,742
545,-400,-581
475,-339,-579
757,512,-407
421,-606,767
351,-669,797
558,328,910
-837,502,845
-524,-438,-520
553,283,835
-559,-548,-440

--- scanner 11 ---
409,349,-680
583,486,597
474,-653,-554
-87,-62,-189
-728,-841,-829
-492,267,-439
-621,-783,-872
-575,-913,-819
-19,2,3
407,553,-663
94,-189,-134
-663,443,543
643,493,527
428,471,-827
688,-619,256
-603,256,520
-792,-780,697
-631,337,646
-311,284,-436
-796,-771,628
804,-633,371
-750,-817,684
660,-592,412
476,-877,-544
381,-772,-570
612,596,676
-503,314,-438

--- scanner 12 ---
-359,585,-724
-632,540,585
890,-796,577
870,421,-615
905,367,-798
-479,-392,701
494,405,863
-720,-801,-885
-439,550,-572
-263,565,-595
-745,545,665
488,463,800
726,-810,522
393,475,886
761,-650,-394
841,-660,-354
704,-819,664
16,-36,-46
854,-653,-519
-725,-901,-793
-800,-745,-831
-663,410,678
-584,-394,741
733,382,-696
-529,-363,594

--- scanner 13 ---
-650,-668,475
-804,-463,-506
-571,433,-601
75,-62,22
-724,472,550
369,-378,312
790,602,-724
-835,398,490
333,730,306
381,-295,265
397,-710,-813
-841,-578,-480
409,635,348
-516,413,-495
-665,-550,-546
790,527,-872
502,-805,-787
-69,-22,-117
-574,-632,560
621,-712,-803
-859,483,636
-568,-568,418
509,624,308
787,527,-734
-461,386,-481
16,119,-42
404,-425,238

--- scanner 14 ---
-831,499,-428
-627,594,628
-694,-814,-568
9,14,126
-125,-145,145
701,-568,687
-638,-805,-544
-799,535,-478
479,691,-641
309,821,737
444,-714,-366
631,-558,851
-781,-690,680
467,750,801
-628,-751,716
-721,661,496
-931,573,-357
-667,-622,610
400,-670,-566
601,698,-521
630,-622,722
421,-729,-430
-712,-889,-510
38,-151,-12
-594,651,498
519,742,-522
356,677,807

--- scanner 15 ---
-655,538,409
693,744,533
582,502,-556
717,-673,695
-371,544,-655
-680,665,366
-25,-76,-32
-395,-396,701
-390,-488,801
-676,-709,-650
632,706,-536
727,-509,625
-315,-450,645
635,674,386
663,-638,624
-852,-686,-665
595,-680,-787
-494,527,-571
663,-750,-673
534,-644,-634
552,596,-571
691,805,463
-756,-557,-685
-383,509,-440
-685,475,339

--- scanner 16 ---
-496,-614,723
-634,-613,-579
365,-589,-674
-414,871,841
-487,845,811
592,770,484
-459,-499,749
592,539,-625
627,690,374
-455,983,746
-130,11,-114
-733,420,-772
-592,-516,-510
618,649,-567
-72,195,-10
-887,470,-814
298,-524,-831
243,-508,-682
607,740,578
508,-309,520
362,-284,473
457,-448,476
-798,605,-803
-635,-527,683
-663,-616,-601
688,606,-576

--- scanner 17 ---
489,854,-602
431,886,568
-650,603,625
-748,553,624
-758,446,640
-435,744,-440
583,-496,-359
-437,617,-450
539,822,-566
-567,650,-507
398,-496,882
7,-11,-31
702,-456,-410
-740,-444,-351
-746,-333,-424
-670,-574,675
-75,142,104
461,806,524
-618,-618,649
-676,-286,-280
390,818,487
418,954,-528
380,-335,859
582,-578,-403
393,-379,735
-696,-704,624

--- scanner 18 ---
582,-598,-217
731,559,-392
-530,-463,535
591,-495,686
-675,697,-705
498,-464,556
667,544,-369
-12,10,101
-681,523,-611
-707,-631,-608
-672,-646,-475
475,-648,-246
-438,-549,604
511,-382,691
-587,622,-618
529,459,746
-412,-364,577
-434,398,954
553,468,690
-523,523,899
435,-543,-248
-733,-609,-438
531,603,-348
-410,450,985
587,384,764

--- scanner 19 ---
516,646,373
-486,786,377
-533,751,303
-820,534,-738
-866,-590,-465
-913,653,-722
527,746,413
570,-353,-383
363,-358,665
390,-464,660
308,-450,756
-626,-505,578
-541,-407,595
-164,50,-12
419,365,-807
-24,-57,46
654,-516,-426
622,822,371
-522,-406,579
-887,-672,-629
494,365,-659
618,-483,-429
-403,774,330
-885,-468,-612
-818,758,-748
419,368,-669

--- scanner 20 ---
601,-381,-817
108,48,-181
-501,730,-982
-692,658,-961
835,306,598
891,558,-555
865,-485,707
-461,-546,701
570,-384,-832
-613,-720,-903
-726,-793,-989
864,478,-583
-711,478,506
-549,-621,614
188,-80,-42
911,-575,703
633,-388,-755
-729,747,-941
-702,-845,-958
-455,-720,607
-599,437,376
622,317,562
820,557,-688
867,-462,649
-673,324,435
868,290,575

--- scanner 21 ---
-917,452,-578
-703,-655,-422
283,-600,769
-657,717,471
347,-664,-613
310,833,-506
-27,74,-86
284,-616,750
467,444,425
-897,-351,888
-845,442,-731
-874,-324,758
-107,-107,104
-617,-662,-422
315,-712,-576
345,591,406
277,-680,-691
-787,399,-624
263,832,-495
280,835,-314
549,608,404
-776,701,378
-909,-398,805
382,-599,665
-881,727,473
-704,-644,-432

--- scanner 22 ---
-397,770,-682
-379,734,-512
500,577,375
511,435,-436
13,30,14
-460,839,-524
-749,-701,278
-779,659,408
-694,651,318
-71,-42,-160
-925,-771,-872
520,579,572
461,521,-495
361,-455,-656
332,-459,-622
525,324,-503
-894,-712,414
-894,-761,-724
-599,610,364
414,-545,-688
448,-504,286
468,-599,325
368,-523,347
-893,-588,276
478,589,498
-930,-755,-733

--- scanner 23 ---
484,-744,850
-838,335,952
-890,359,921
558,-815,950
-765,606,-644
-666,512,-651
727,-650,-500
12,-88,-40
702,332,904
433,350,-543
685,560,945
392,462,-413
-729,-806,-425
-124,-78,138
279,388,-472
-829,-604,713
676,-531,-460
-744,-742,-402
-685,-606,-381
613,369,924
683,-651,-582
520,-694,818
-820,-628,657
-904,-662,731
-591,600,-738
-765,448,866

--- scanner 24 ---
-563,-459,-728
664,503,-669
884,-724,621
-623,621,-698
844,-669,-731
82,-105,-74
-790,607,393
-845,578,-713
-21,13,-182
-583,-390,280
787,525,-657
837,493,519
748,-869,632
815,393,443
754,-754,-739
-422,-491,-656
-763,417,398
-490,-419,448
798,-574,-690
876,473,424
-569,-606,-671
-720,544,423
-588,-345,355
886,-868,508
-822,615,-717
590,545,-659

--- scanner 25 ---
-353,-781,-678
300,486,975
-5,0,61
-511,-560,720
604,680,-335
566,-432,-366
611,766,-335
-768,726,558
-13,181,194
-448,-740,-790
-493,538,-644
595,-469,638
-445,-736,692
-471,-699,807
593,679,-345
-503,466,-491
580,-438,-633
-383,-708,-652
510,-545,602
347,474,892
273,509,845
-752,607,465
633,-401,-465
-450,596,-537
-778,502,560
453,-463,702

--- scanner 26 ---
-7,43,-97
455,738,-376
-667,682,-351
425,-622,-506
310,798,626
279,808,774
807,-733,584
-723,-867,-447
-921,-362,480
-744,723,-351
-114,112,63
605,-573,-462
825,-697,414
510,-614,-416
311,625,-374
-566,780,-368
-536,-875,-430
-745,748,656
-611,-813,-370
744,-802,426
310,749,-512
-797,-353,572
-651,731,572
-761,849,530
-858,-308,428
274,792,635

--- scanner 27 ---
634,726,880
915,-303,525
-431,-500,-414
876,-503,-640
885,-451,-678
896,-316,764
-515,645,434
724,804,899
-661,598,409
-431,609,-645
526,531,-562
-658,-549,714
-566,601,573
-405,-442,-524
130,131,24
912,-399,-637
-416,703,-615
-335,-451,-481
-725,-706,649
-396,499,-565
603,400,-506
673,461,-504
750,716,735
-780,-557,633
916,-301,608"""

FULL_SOL = []

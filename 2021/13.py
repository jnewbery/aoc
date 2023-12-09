#!/usr/bin/env python3
def part1(ll):
    raise NotImplementedError

def part2(ll):
    raise NotImplementedError

TEST_INPUT = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

TEST_SOL = [17]

FULL_INPUT = """938,670
246,156
622,476
137,296
708,323
1019,283
415,505
1043,234
666,871
157,893
969,266
1280,690
987,260
296,428
1302,361
92,168
206,204
937,659
551,488
147,456
1279,42
463,154
407,266
1153,893
495,372
733,459
378,169
48,705
31,852
577,571
36,672
1014,661
441,880
1305,791
115,553
455,267
360,833
915,455
346,53
606,367
1014,513
930,633
190,350
564,577
1205,376
928,462
577,435
825,686
517,598
782,119
1110,539
67,236
77,185
577,723
808,855
139,742
865,414
159,522
1159,626
440,58
743,505
252,502
1190,659
855,521
1094,185
798,176
1114,61
174,695
427,581
161,670
74,222
1250,829
930,261
398,497
541,47
340,102
1057,614
820,753
1057,453
1158,141
492,499
267,234
642,568
904,586
1274,47
169,781
241,164
1037,621
50,254
44,63
388,561
1099,522
1255,809
736,171
1139,145
323,708
928,686
527,851
478,771
895,505
320,455
156,268
787,399
1136,695
150,751
252,537
1242,631
468,40
436,208
380,261
324,3
954,93
946,504
991,817
604,177
565,348
705,406
89,38
735,418
234,161
880,0
956,553
523,847
654,753
946,266
465,822
768,282
3,5
18,513
758,737
980,639
1248,725
1250,570
807,716
1138,375
1076,354
922,561
417,434
831,626
115,861
1255,710
793,473
77,499
964,169
989,343
875,183
758,224
398,397
1208,670
903,266
77,403
82,176
427,313
139,152
810,550
577,619
867,665
443,665
485,775
272,686
196,833
291,163
1029,387
1221,38
1019,611
544,78
299,826
1289,854
1160,751
1230,469
408,290
1056,176
281,507
170,828
18,828
1175,329
539,413
698,764
373,59
433,376
1020,504
85,771
151,716
934,245
172,792
383,78
1223,725
348,278
3,453
152,525
1037,618
1197,686
319,749
328,318
623,42
1258,521
441,14
862,802
1233,459
1140,791
994,509
417,262
517,712
1029,507
52,821
984,133
1120,96
1186,764
482,760
1114,754
190,96
728,494
1071,602
1019,122
92,726
1221,856
710,686
1140,49
485,208
661,775
774,511
154,123
383,816
986,3
455,409
200,614
584,749
616,662
493,353
572,649
80,171
932,177
1237,614
574,171
480,247
656,193
1153,449
502,257
1303,632
733,403
1274,672
872,515
219,631
353,9
1020,47
683,602
62,169
734,586
325,614
482,323
1160,143
987,5
982,766
1115,495
1086,894
441,546
816,675
1272,662
929,618
865,480
237,262
729,728
1197,159
880,289
68,148
816,227
924,198
113,686
704,245
745,486
500,550
510,824
817,353
708,571
1021,77
929,276
704,79
1061,51
1002,514
351,152
934,693
216,709
736,469
130,385
1221,546
276,254
1054,556
1164,7
2,107
812,626
610,383
1069,164
738,848
462,73
618,579
299,516
126,775
415,389
1044,113
1115,47
1062,586
746,129
976,397
1309,166
602,323
494,227
888,820
835,662
728,400
1009,397
410,718
273,618
253,453
865,59
528,775
1002,380
224,446
1305,327
364,166
189,744
67,658
1307,67
572,848
957,9
454,602
743,837
811,593
113,882
77,275
1232,138
482,326
216,653
987,827
984,761
1121,150
90,765
274,323
701,123
308,514
1159,178
80,723
1154,268
1255,16
20,77
745,856
729,726
628,229
475,662
120,659
1091,711
688,476
500,312
408,171
996,543
323,453
826,66
508,775
89,632
601,52
686,18
638,455
1094,67
562,509
102,593
517,312
435,263
594,829
930,323
1073,348
524,509
659,653
895,690
443,372
1149,670
763,408
160,227
36,628
571,28
687,70
1307,889
200,539
87,243
818,753
1230,873
152,173
408,738
219,711
890,845
606,79
1168,77
1200,78
688,154
335,184
629,173
793,712
318,571
769,686
1310,141
234,354
3,403
155,322
579,516
706,53
977,241
1178,652
1054,637
5,791
316,593
681,528
226,152
838,53
316,301
947,283
647,262
833,427
1014,233
1058,502
562,207
224,894
836,775
869,14
256,273
541,686
1227,345
1074,99
92,562
489,306
1149,801
172,760
811,301
1230,425
512,718
1084,152
213,14
813,445
628,665
1011,516
850,773
21,40
1033,406
783,43
719,840
1225,164
219,152
1222,173
1038,686
236,99
1220,99
761,824
909,814
740,756
676,278
219,183
1218,168
1233,485
281,682
403,465
672,455
1037,276
649,775
622,292
1303,262
435,94
68,631
402,201
326,133
574,51
986,891
1120,350
912,621
970,792
549,824
253,677
536,292
1290,177
28,190
356,93
842,40
769,208
653,877
1215,460
803,8
1262,245
417,348
865,507
1116,325
580,828
314,211
1233,185
582,624
818,499
661,464
726,749
933,488
77,459
604,702
454,7
435,711
416,873
1130,439
137,312
113,208
582,494
1138,102
924,310
281,387
569,663
652,143
353,885
602,633
816,219
606,649
191,565
55,464
846,96
422,759
253,441
560,311
36,679
1290,525
1158,173
333,775
704,649
527,857
692,579
72,176
584,690
562,687
1121,822
599,246
319,593
1124,488
657,877
457,675
1179,266
668,568
577,171
170,845
865,387
452,578
174,141
119,203
70,674
745,348
12,326
1240,749
239,389
574,313
709,52
542,282
31,824
110,368
182,219
353,437
755,133
1029,212
571,866
494,675
715,212
920,844
1181,667
704,525
20,369
729,814
1168,176
290,119
1196,143
748,338
1183,25
221,376
1258,883
331,226
700,383
731,516
649,430
227,502
783,3
959,152
440,836
726,369
70,749
1171,152
897,388
154,344
661,430
994,385
507,8
800,70
739,345
1192,511
478,751
853,890
298,821
808,39
687,852
254,176
127,473
1195,553
733,619
214,58
788,793
723,455
465,150
10,471
373,235
623,294
281,212
1016,173
912,257
1061,388
1190,235
546,656
378,389
676,616
1240,397
783,409
400,64
569,282
1292,841
663,262
1262,705
457,4
1232,308
226,742
649,327
952,381
567,651
724,263
940,316
956,240
53,500
1298,326
1016,866
1223,690
688,292
1076,332
632,782
454,740
131,495
152,141
989,653
189,488
1086,224
1072,873
651,515
870,58
932,169
1258,409
700,511
769,735
5,567
321,241
200,740
576,586
581,726
303,742
132,652
1014,428
380,633
330,815
73,280
1207,488
536,511
902,604
446,852
448,11
77,485
594,65
1039,78
708,11
482,550
331,345
373,771
333,103
959,742
1220,795
36,215
848,821
726,145
482,568
682,665
937,771
298,353
774,383
28,373
826,49
364,266
716,0
883,581
1094,795
212,306
136,789
401,814
659,889
422,74
541,208
20,817
364,728
785,785
937,212
1104,204
74,290
855,309
7,856
587,439
663,38
174,199
282,679
1120,798
845,582
290,847
92,332
1243,236
1020,266
443,105
497,449
728,270
124,764
1280,513
535,203
741,771
278,201
708,633
599,269
842,854
994,301
18,841
324,891
480,641
740,138
95,882
734,308
577,282
793,296
932,389
705,488
52,521
180,455
1190,540
581,814
420,637
160,667
478,359
190,798
150,143
130,826
89,348
569,123
771,301
853,442
1146,753
733,395
348,333
441,287
216,99
3,67
176,183
547,856
68,711
605,406
544,627
105,152
856,103
1032,201
618,131
599,878
604,841
1233,275
479,626
1151,522
21,854
668,543
1028,740
113,159
746,577
586,863
1247,840
272,208
201,138
249,58
159,372
87,725
776,540
907,579
1099,677
468,854
748,687
303,152
1094,241
52,373
85,739
48,189
52,883
157,445
430,0
185,234
127,627
6,887
527,627
582,176
1118,521
216,67
386,198
1150,227
172,344
687,600
120,690
387,712
1203,632
888,123
689,676
468,488
933,770
199,267
256,497
586,263
895,389
110,627
479,268
741,730
694,232
666,301
704,490
129,667
1242,711
830,641
194,325
618,315
910,64
1052,298
1171,742
869,546
1153,880
1148,128
381,173
1233,11
1240,130
103,488
274,267
402,693
594,381
495,267
246,425
1292,268
602,37
539,677
793,421
711,16
89,856
1073,460
1020,180
763,856
438,205
365,817
1210,600
372,224
135,565
853,452
239,242
363,283
1079,348
142,176
107,632
534,242
530,130
142,77
1290,77
1218,385
249,51
214,57
687,42
972,77
1173,296
808,305
813,1
1225,155
333,791
774,607
1300,23
1140,103
340,550
154,582
10,423
38,662
565,856
354,688
333,241
1256,208
272,656
736,51
880,672
1145,894
1022,379
566,721
668,102
503,716
912,497
610,511
1292,828
282,222
22,782
572,718

fold along x=655
fold along y=447
fold along x=327
fold along y=223
fold along x=163
fold along y=111
fold along x=81
fold along y=55
fold along x=40
fold along y=27
fold along y=13
fold along y=6"""

FULL_SOL = []

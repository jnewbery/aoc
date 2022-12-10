def part1(lines):

    sol = 0
    for l in lines:
        line_len = len(l)
        front = set(l[:(line_len >> 1)])
        back = set(l[(line_len >> 1):])
        dup = (front & back).pop()
        # print(dup)

        if ord(dup) >= ord('a'):
            pts = (ord(dup) - ord('a') + 1)
        else:
            pts = (ord(dup) - ord('A') + 27)

        # print(pts)
        sol += pts

    return sol

def part2(lines):
    sol = 0
    while(lines):
        ll, lines = lines[:3], lines[3:]
        # print(ll)
        # print(set(ll[0]))
        # print(set(ll[1]))
        # print(set(ll[2]))
        badge = (set(ll[0]) & set(ll[1]) & set(ll[2])).pop()
        # print(badge)

        if ord(badge) >= ord('a'):
            pts = (ord(badge) - ord('a') + 1)
        else:
            pts = (ord(badge) - ord('A') + 27)

        # print(pts)
        sol += pts

    return sol

TEST_INPUT = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

TEST_SOL = [157, 70]

FULL_INPUT = """WwcsbsWwspmFTGVV
RHtMDHdSMnDBGMSDvnvDjtmpTpjTFggpmjmTFggTjmpP
vtCSGRMBDzHddvBHBzRhrlcZhlLzWNlqblhzcr
shhszHNHHZWqSzVNdClMjlFjBBbNTB
tQQGmnrMnJnGfmvrRRPCjlbljFBdjFCjTjnP
mRwtfGrMmJtwRDvQJQrJpMLSzVDHzhzHZqZzqSzcWVWH
WsWWgrtgsrhTQtsFcWPcRMCCTvqvMvqNNqMMHlMq
bBJrBGbzzLJznJrbSDGGJLqmlvqMqvlmLHRqRZZRNZ
bzJfDGVSzVrJGwjVGPPpQthdPsPpjdphsc
pJpCCBSWlczWWBWMHdMmMsFmpddrgF
wfVqZZGVQvzsMqmMgHjm
vDZGvPttQTVtGDQDDDGwbSCcSJSCJWTcRRSRczRJ
HLVHsVWLwbWswbpWFWrrmThfTPNnhNSDDNhDfznTnhnS
pBRcvGvvBtpGcqqQvgcphPfzfDGhzdzPDzDDhnhS
ZQRvqBptjJgZCtJqqMMMLHWwMWZWHHFFHm
PvPFPvLLLSvNFvQNWNPvrPLrZjwhMttTwtTtQZBwqjqtZqwM
HJDDbHjgppzCDCmzpgzsGbCsTMZqZllqhJBhMTtVBBhMtMth
zgGncmGGzHCnHDpDgDCGsmFLLPFjPRRWLRjdcjrcdRLd
zHnWzntnBRWTSBzRBddpFvZVcHpLFvjvLppvHP
MmmWmNGQhbCpZVLLbccvpj
QDMCGrNWfwNznBJsJzDBdg
tcRcZccZmdZJctRcjrlhNNDfrdNdSfNsNT
QHQpBVvMpRMwgBgvnHRFlhrSsgNFThgTFFflNS
vvHpVBBBGBppHvpLvHGbjmmtCqWLJJZRzZZZZb
ZBtTDZRWsTsDZVWVZDmjpbLbpSSzmLpWrbrS
MFNNFvvwFHwlhmNrCStLNtjzrb
vwffwcHwflGqGflHJfDBBZtQVBgZQJtBBsnT
pTJcmMJTspmpMZZJJZHCQQMzPBlQdWWWFzWP
LDnwrdnDnqjfqgvfDjrfFlBBPFHFSHPQCBvQSSWB
nLbjgLjdbrwVRcppsscJVRRR
mHnfggmMtpHPPBCs
PJjlQQRrJhJNPPTtBsCbCCTlpptd
rSSDhNQwShRRjhmMPmzMDfPmfLzL
HzLFBgrCthtFrrhFSCCCvBQNRVmJJJmnpnddmppddVtJ
MPZsjDWPjZsVzNTzpVdRdZ
qMfjWfwclsPsjwzqHgLFhwGFwHrFFrSC
llllmSbhNmSbNzlPmRNCcgLLchHHpTGsCTQGpT
dVjBrvBBVLJQsLpC
frZBWBDMFndStFsSwzlPlq
vmTVVtmJHwCwDllttTsrcPcMrfqPMMpjMq
LQGBRgGGRNgGgBhgzHfpjPqsMjpLcLjrPLpq
BdgzgSRGBnNHJtJlVStVmt
FbDQsFjPVHFZFSbrVjSVvMJlGBJhDcqBBllJGccJnh
RfTCTTpmppfgwCpwpLwRMnMGMlcPGqhddPcJnl
zgLPLNCCpLggzmTzTWmVrjVvrNvjjjvbVHQZZH
RBjjpwmRszBdvhLdSvpVpV
GrbfbJWmQJGWrGZZQMbSLggfCgSHhCSgShghSC
DWNDZQcrbWQrZJZGQQZPsztzBsPmBTzwcwRwjT
rlvgglvZqbrbWbWWdvdmPHBBNMNJGqjGRRnHnPBJ
cDFDcfcCDhLzsCfLDVpGPRJMPsRJMPNRnjHHGJ
DCfMVDFVScVMVQlgmZgdmWQQmS
nWTWWgwNgGDdBZBVcvDzzJccVlCzHD
RLppMMLpRqfMtMjtMCHJFSpzHSvSpczJdl
RdLRbQRjsRMrMRRMfbQLqPjbmnQgQWWwZmggnNTgnnWwhBhn
TmzjMjrmjmjBmHLvGPpbvWGqJzJJ
CfScwNDssDVCccdNVcNDQfbqJLqSLPpJpJJvJPpGTWJb
nddCQTfQVVrHmjMnrMFM
WHDnTwvwcwZmWwQTnBtgbVLLbgfSlTfrfb
CPPGdJRzNhNpzPJtMgBLbgtlLLfLMz
GJptpdFRhJwDmFHDjvnD
PNcWDNnNDcLjDDcSRWtQFfzzzQgPgsssZtPZ
MGhJRJGGrlpVGVHVCqqGqBQvzFzFfBvZvvtZtvFzvZvQ
JmJplCrlMNdmjbNbWR
pqpqFJPPSswJshNghg
zTHHrrbLzDQHccfhqmDshgCwfmqm
rtqqtTTHtzGLPWBdnGBSWGSS
gmNvgVqjjqzfMRgrRtPcft
WswSQwWWHGCsHQhlGGLLJRbLMRfRGcMb
dQCRCWhhwCwFwQshhRTmmBmFjFTTVNpqTnTj
FZvqSWqjjZvvrNSvbblcbslDppDHbcsS
MmwLTwPmBwmLJJmLlWzWnDllHcHzcDHM
QRwtQtLTwwQBTPfFfZdFvqqrFGWjrh
MqlnnNvJJZnNNdJZZLvLJnMzjjCTCChgWjccWqcjhcgcWR
tbddSHDBbHgHhHTCjh
mffBfbpsFSdQQDbQsrlJvwJNLLJMrrlsJr
RjqbNRRbDDqHndbcHDqdRHcChsffCQJJssZGpzpCpJphJd
VrMmSbrWVMtMtLmQGCfZWJZCfpZfJW
PgSPgTvSSHjjBbvbvq
whclNQQfcCFCcrJRjmmHNWsmLs
PPzMbqBPLVtnTppPTPzHJrGWJRRvsjjjRHssRb
PtgPVZTtTLMtBzqPqttPVMClcdDcgCCfCQDSdSgCwlhh
DrcrsvcNtLWSFPSFszbM
HqTdHJdQhGJBHQHWWDTnnPzbMMzPnS
hdwfqdhQJfjlccrfvNDLfl
BBPCWvjvTLrHTHHPCTndfwhbdnnZZfDhJwfJVb
msmgNMMcgmgczlmmgQNlddpVDDZpZpDfhZfJwsJF
mmQmMgSgzmqSRllGmgjPHrvvwHttjLrLRWWB
RwvDvhjhMvwlFNwNwCWCCWWLZcbGGZLGJVrppbZVcjmpmJ
tfnfsStnPPfTfgnPSSzPflJZZZrlZJVzLLmZJrzVmG
nPHqgfsHQnffqgSTldHTPnPHWMRFFqqFhNNNCwNCFMMhDMhh
FmwFHmnlGJfnlSlmrfsSvWgZNWNvLvtqLqDJhWJD
BVVTTMqRWvRZRbhW
pMBPCzVPQcQsGqSFmPFwSF
TcpTpwqZqMpZqlZCpZlwDjjcPNdgdPjHHHdvhHQgvv
zQFBRbmsQbLLBnGBvFdPghddNgHjNSSj
QnszWVzLfsLGbnGQbwpVtMrwZTqpCqpppr
WrZmrJcGwZdGZZmHdJcwGWcZsdFFLqTtLVtSTLtvvLtLLqSs
fnpCCQClfpQlzbbpQpflBpjhLVSTvFhjqtstVsjtstFVMs
QBQRnbCRpnPngnbggCzzRClZwJHFHDwZJPJGWHwmNGHPZr
fDhjvftQtDwgPhdRcRRP
bbNSgllVNMCWVnbWmcdFdmmFdpFpRrPPPw
NBzBglNzBvvGZDJQ
rGbbtStjSdbGtDpjjJbbRRbdrcCsCCrFqhllrFHsFsCvqCWH
TzgMMgmTVgzzTMLLfMHvTFsFCqHTvFsTvshF
gLMPBgQmQmNzVZLPzPppjbRhhddGBGSttbpR
zMJTpMzpVczHbCzVJVFCpJPngnBqVZqsRZZPnjqRgmjR
wttwNdfLQwLhwhhDDhWvgRmnPqsQqjnBPSZRgjPS
DdLwGGvNvhlvrrMFlFTcZrpC
llBQWMScQlSSBjMrvrrPpFHFBDFDFJTmTtFFmF
nzZzfVgzCNtnJppDHPnPpp
LdRNfVdzbzCCjcvllMcsbtjj
pWFwpFhprTnFfWwZrsBDmsqBvZvjjv
VbcHCthtzQtNqBsvsZvQmQsj
cltzzVcJSMtRWdhJLhRwdh
lmmmLRdZnjBlGgVhNSVvRMWN
bDwCqCGPbwpPwDPPpCpqpPbScvMSMSDWgVcSShNNVfgWWv
bTpzqJHPFFJqbTHswLlGlBntGnjQtGBZTT
pVjVlDDhmRPlHlHPWzWVWrVrcWztVdzv
GCqGGGJSFbnLJLLfrLfPrLdgrrgfWd
PbJSQGSsGnbMbqSFGBMMbsGTNwpTRwppDRsjwlNpsmHwDl
GcnPbbbLqDPDBPPDlQ
JtTChNfRpNJMTCfMTlJVsdVHvDddHBVmQm
TzlffWNfjTfjjCjfTtRrLgbnbbnSSwbnLzZZzr
hggWzjLhzhLhjzVWgpCpTFFHtCJFTJTHHHdG
lvSBvNNSNSSmlbwmMJCGtJQCHmdT
cfSlSSlvBDBPnlPPDZLsgtggZZVVfhzRgV
gGVJGvVVZZLvQLWQppccpctpNptMhnhSjjnM
fzQBsBzmwPzdQrRbSFNFnsSDchjnFhMN
bCwQRbbCJvlGCHgL
NMgdHVSqgQcVHmlllLDjlCLdjL
whTRJtJTnthWBlLLLmlFtVmV
wRhnGTpzzTRnVbzzWWbJwbhNQrZHfpNgMQpfZQHHNZZHHQ
qNNlMdbNrlVsQQfswQNCmW
LJzBvSdLSHpDJzzzHJnHnzFQCCmmswmfwBGhsQfWfCwW
HzSvHppDDRvgHzzcnqTrTtllZdRrbRVVZZ
TWVVVFVPpjVFtRfPBmmzMMPCvmLm
hDDrwndQQbbhZDMSMvcflMLmfnBL
grdggqsbrhdJJJrhbwbbsZGHVNHtTWpVBFVTTTVTHtNg
tLbvnTCzCVnzzwVTJVlwltMFvQFQRFFrQPBFdNgrMBNF
pShsqqmGjZfZccsqSfbdNBMMRQGBPgMdPMPF
HhspDpjhSjbcSmcqhZDcZZjTttLVwlTJJVWtnWVlWHCltL
DwQBvwBnBrSVRrZM
JWWGRssgRsFgzsFPJrNHVMHrlVrPSMNjHH
gspgFzRCFWLJpgqqRWgqpCJwnQCnhQvwcTdcdddnwbDfhf
fMMCwFDGNNMTdTDLlVlZZmdZBdBtVr
jjpjtbpRcPvSPnPnpPnvPPPnbZlmrWmLWHmHBWHlrmrmlZWl
jqjjnPqngtQfGFftFq
qnzhhbzzqGgsqGtnwcJrlCMlCjvcCCcrCRrvCv
mVSNZdTQdVVWmVFHQrpCjpjDRvjMRjdLRt
WBHZTHHTFWWNNBNHQTZPsPggghfgsnsgsffthszJ
sDwpdMgvHrZgwbdggzZZgPhFNFFcjPPqhLhjMlPqLq
JffJfnJGtBtCQQRBJZTQJJGfcNjqCLcFhFWCPLjhFLPjcPhl
VZZVmtGQQZmHrwgddppb
NNNlpjbVpGglNbvpTwBQQvfWvfBrWvBW
JthDJsLhhHPcGcqPshJsshSBwCWwfWSLCfSfSSRBrfWB
dhDtZqGmctZDtZHqDGVgVgNbbbFjndMFNlFg
jqDVzzDMdDwsVQLCZVCRWLGBQC
bbHFbSSpFbFHJHStJNbtJprZlCGLQsLGZRBLRQLQpLBClZ
SmFmTPJvFTNbmmsMdqqjscwz
RqMbHGJRJpgJgGgQjgrLTrTzjcrTrrLg
lwfwdhnflPlbCsVVjhCSbV
fwnNtwmlFZpbFZtM
QNSQrLTNrLNQRRrfHFrSjqhblWtSltqlWqtWWl
DvgBgnzgcvVZMljv
DGJdjBPDngDnDjBpBmFpTRmRFLRRmmCmHH
dtgSdTqdlvdJJvFqTvSqJqqRMPBtLHPBnWbsbWbsbWtWtWHV
DjfCfmcpNrwZQCmmNrDZNZNpsHLHWBBbHVVcGGGbHGBbMVMB
fpNjCfzLNZjTllvzdSgFgJ
nHBfZmHTRwsZffjBnHfmRZHtLtdNPPlWvddWLWJlJldCldLC
zwrbphMMVFzMwdCWNPlCbPdDCD
hccMSpqShMSrhZTBwmTqHjqZmf
NJGGLwGsTSsNlJZhmtgCVlbWQWlQMtCbvb
pDjppDBRdjzqpHqDSDzjVMCCrCrWtgQWdtdQQCdb
fHpfRBPRzDpBFSqcSBRBSNhPNwwNNswJLhmmLNGJZL
RZbsPgnVDzTJcdGjDGmD
NwfQHQtpfppQhjVVjqVNJJTN
tLLtwSptVCSWpvVtRnrbWbMgFPMsgZss
VsQjSwwVSwsZzsvdscZvfrhPRpqBrBrbpzMrrTMh
JtNDTmtGJTmLCGFDCHtDhMMBRhqqRbPrfrbNRrbR
GDWLlDnFgZdTSTWv
gfQHRRpQgRqNSBtjqwjztzjtnL
FvsPgvDlFcmvmTLlBMVztnLwWLzL
cvZGDcvbPcmbTbrcDDPgvbTJdJfJHRhZSRSpRRfHdSpSZd
FGHHHWvBWrHHrWVZJvVtcSrtrTcrtcjMTjStSM
swpwfRhRmmmRQDzcJlcqMSMMqtbMTz
dQDRDDRQfmmQDNsLfwRJvZJWFWVnPWvvPddBnC
zVhHvhMVTnMJgcTzMcfGJtfBWRtBRqJWtqJb
hlZjZSQCZtfBbGjqbb
SQDNwplrDVnhDcVHgT
HHZmttZVLVMQQJwMfcDRfDbbMN
phWvTgBqqgBWsTPTzhWzhzfNGNNwfqfcDwJRRbNcJcbl
FnTsvnhppTPFTBpPzPvpBBpFVmtfCjfmjtCmFdStLmtdfjSd
hMTPPMNlLZNSGNbRBB
gjmrsrttsCnsCsttVsjvttvtZGFHdbZGWWWdZSWddBHHnSWH
BmvptjsrfjBgsvvfgmfQchMpMqqhcQPMMPMhLQ
dJHGnrJJpGpDpFzzDmfsfSSCbfTfMbbRDb
vLcwtWNgtVtSNWmTmTMCmhNhTRfM
jqVgqVvWwwLwwgqZgjVSrPGzHHHqFnrHnFGHJGdr
QcQcdgbzwJnzfgVnVwdHQbdBrrpplHvmhLjrlTphppLrjl
MsPssfSZMWGWqWssSNPqrmmLBvjhqTvhjBprhB
GRDDZMFNMGFCSNWFPDMMFWNnwVtdVdQfcgtddwQwzRJfQd
pMqCMBGpMMCnwnpBMGBlbVRFJFWsJzRdzHlWzzJdJsJd
jLLZjDgPbNPZTDbvftvZgzRFsRzRrRRHWFsJsFJc
TZZLDPjtmDmbqQGwQnVM
RjnNhBnnNNmJmBNhrqGpsHbHtstgTtTjqb
WVMfWwQTzWZDMtlsfldqpplstf
WVTWSTzwQWSSvQVZCQPTSZPvBcnmcvnrhmNcRFncNLRLJmnB
lffQcnNTQBBcwqsdcqjSspcWtD
MPMGrHGMMTqWTtDg
VGRGLrJHZzLHPzTNTmmBfZQFTNBQ
lQBPPrBrlnqBgSRhgZZZrLJr
VNcWMDZbJHhWfWff
VwvMwMvdwvdwjcwdwDDqsqsZQqPPzqzldPQtps
VVJcZJVrRSdcsddfsvvbvFZBnngBMzMZFD
hLLqLpqqWWphWjhlGlCHDFgzbvFBbgBFtnQpnngg
HlhlmmHBTqTHHmlLqjTGhHhPdwdmsdcSNSfNJRrRcfwVJdrr
HmhvmRzzHHrRMBJBjNJGDJRnJD
cbqcPqLWZwsgQWZwWPwWgPPbntJnrNftNNNBtNJJNDBNqdjB
lgwWgggQcWSzrlTHMHlp
FZhQpClCWLBlrNDZvrwrrNSH
ztTfjMjJjgsGrqvzDGwG
bMjfnjndjnJtfgMTwPjFhQhCLdQCFWQQLWQhch
PtrqPrrMCPChzCtLFRbtNgbdTjbF
GdZGvJSWWDGplFjbjLjLSTlL
vspvnZsVppBdBnBpDCszhzMsMzzPzPhcPC
PdCtdfCMfGmtfmtBSWrMQwSlwWwJNQ
qTqbcjqHTZTbcDqczTjjZvWrQvVWJQSVQZZSVVrJNr
qbqjRFTcHTcDFgcczRqFrPsGGGgnhtGssCdnffGmsP
vVbcMvqjjjmHCBCBBmBSSH
PzzLTrcrwQgfLGrJBHSGFSCHtRFBJt
cfsPrLDwQNgsrTNTQgLwVpWnVWvMNvqjjqvpMvlj
jbqZNjLbZQvcfhhQ
CWdCDWWMCgmJDnJmdQVzMSchvfcQVFShzf
WPgWGRWRHdPBsttrHvNtrl
MCJCCMCqcCqJsnssjQRlTvQQQQqTvqfQ
HGVmwmLVlZRzcGZG
FcchHmDFpFbDMDMbntsJ
vfNvvttvDRcrvRNRNTLDNRcVsFhwVBVTwbbFFVbVhbJMBB
CJGgSJHdgPPSnQnjnddHGGFMSMwMMsmsFMMFhFShMWMM
dGCdjgzHCPPGlHDDqJtqRcqJlpfR
CwtqqvwLwnwhtRLtdRnwnnRhPHpLLppTPPpTVfTHzJWVLTWB
sGDsZDllDrMFZVmGgsmDMlmHpJBHpcJFPPTHfJJPzfTHWz
srgVlGSgZVGGrRvwQwdqwtCvnS
MLPgDrgLzThhCTgg
GVfCbvVbVvhBHlmhvhHv
ZqRQffRwtNZWVZfZSMsSssncnDCDnL
VwBNhNNmhJswqjJsRzPgDvSgJvtgvgDt
rRMblbHFfRrSWvPPPgMzLW
ZFpFpCcprGfbrGfGCHclZfnGqmsjmBdNVjQqRBnqBsVNQwBh
VLQlZWQbcPgcPmWbgmDWLQzdpGMTTqdpMTNsbGsNpMSqdq
HChrwfffhJtfHwJTsDqThhDMpTGsjj
HvffCrtBzclQZvQD
dCBVJJmrJDlBdQJWZTTsWbdWThWpbM
FHjSPjwqwssSgqTMGbGWhTMHMMZG
FwLvLfLjjSPqFqgzwffFSvrlDJvrQrDVrnmBvrJsQm
hZCRbddrgrRSVgcGZjjLFGLZFQFp
nzPvMsPvtmvPNssPMqpcWVjGGcGLlqGcGN
TBzmTmzmVmrBSBRrRgdR
bwZZmwfFmcfCRswNWNBsjC
VDSdglSStRCCTNCD
VVVppGHGlrQnnGJbMmnmCh
nFhgnFVNtgtFVssgdgVtVtsqJPTNJvDSNqTZZzbzTDDzDq
HqLHqcwlBjLzPvPJCCvJ
HGrlHqlllHBppRrlwWFnnWfFFVhMnnWdFhfn
FsMFVszjggMMzWlPJlPPlLQsJv
nqnBSNlfZqSvLHnHvWLQTW
hShpfCCSRtfjgFjMzdjlpr
jsbDsQnnwPsFbZgSltWGdgJgpnSp
SCVvLhLRrzCNBhrCvddMJpWdWGvJGlgtpv
cHLBBVCcCNHrbcSQFwQTbDws
rMlbLgrRgpwTDbflcnHtSScwHdJdwHJB
CQCjjZPzGGzCzZQvBVBNdQNSJVcJ
jsPhCzhPqFZzZzChFlsbRRLrMfTbbcLTpD
dqjzmmmQBjBHCmWrgVGWrrrvrpgVpM
PLJnTFbJnhTDzrGgMlvrFMzF
SssPcDttntDSsLcCzHBmmwcmZQqH
fFfFSPHllPRpRfnmmFfHvHjgbsBQjsptBdBTTddjsDdt
ZqLJCLCZzzTgWjdzDjzb
ZhNLMrNcGrchLqcCVMqRvlSnFnRnmmGRggnPnP
HMCMCMrHfwMHtFwTtgHHbVjjbsRZDwDVRbZqjhBD
cDpmpdpNLNDcdZjZqZBNBqssRR
SLJSdPcznSvdvDcHFCftFTFWCTHnWt
NlMmlPClmdGldRZHJs
tgJJcJQcntHBsnBt
TfSgQhhccczSVQqrgSgTjFWqLWmwLFNJLWWPPwqM
GGwTHqWVdnTTVVqgngzzqHzGFbJspFccRsjDpDcjsRFDsdjR
rtLflllZSrhQPLBtQStZvhjDNjbcDNDRNFjCsCDCFs
mPLBQPtvtQZtBlLSmMqVGwHbVMqTHWmz
VvJCrqTvPvQrCpRNVRFGfZfmfG
HMzsdWsjhZSsJJZNZf
wHlbjnlzWCvqJBQlrD
FnVRRsVdSnSnFSRqTVdqBBDBhrDdmcddMcMQMhzm
HtZvJwHlgjlGlHJLNjJrMmrcmDQfDLczDrMhhh
vGGpJjttvlZljZllZvJZvwGqsSTRWSCpnCWTVPVmWWTWWn
wSHCNwwmcSMLSDFcwwSSHQvZnQjLZffZjZZbVZjVVb
JqsNJJGGqprJNtpWhGhspfnffTnTvZvVbZnTrfBQvV
GsWhdGtPWpghJRqhtNPmClczSlDglHMlczmwCH
TzRpjVRjFpVLTTdgrTgrGsZwrZZwgg
vQfSBdbDbMbQNBJrlhmGnrgrgwZhvm
SHSCbdbddcVWqqFPCLqR"""

FULL_SOL = []

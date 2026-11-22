$ErrorActionPreference = 'Continue'
$root = "E:\github\music-wiki\.agents\worktrees\dsh-ee5c71d0-e1b5\local\workbench\scores\score-r3\downloads"
New-Item -ItemType Directory -Force -Path $root | Out-Null

function Enc([string]$p) {
  ($p -split '/' | ForEach-Object { [uri]::EscapeDataString($_) }) -join '/'
}
function RawUrl([string]$u) {
  $idx = $u.IndexOf('/', 8)
  $hostPart = $u.Substring(0, $idx + 1)
  $pathPart = $u.Substring($idx + 1)
  return $hostPart + (Enc $pathPart)
}

$MZ = "https://bitbucket.org/musedata/mozart/raw/master/nma/"
$BH = "https://bitbucket.org/musedata/beethoven/raw/master/bhl/"
$SQ = "https://raw.githubusercontent.com/OpenScore/StringQuartets/main/"
$LD = "https://raw.githubusercontent.com/OpenScore/Lieder/main/"

$items = @()

function AddMd2($slug, $name, $url) { $script:items += @{ slug=$slug; name=$name; url=$url } }
function AddRaw($slug, $name, $url) { $script:items += @{ slug=$slug; name=$name; raw=$url } }

AddMd2 'mozart-k550'     'k550-mvt1.md2'  ($MZ + 'sym/k550/editions/public/score/mvt1.md2')
AddMd2 'mozart-k467'     'k467-mvt1.md2'  ($MZ + 'conc/k467/editions/public/score/mvt1.md2')
AddMd2 'mozart-k467'     'k467-mvt2.md2'  ($MZ + 'conc/k467/editions/public/score/mvt2.md2')
AddMd2 'beethoven-op61'  'op61-mvt1.md2'  ($BH + 'conc/violin/editions/public/score/mvt1.md2')

AddRaw 'haydn-op76n3' 'op76n3-02.krn' "https://raw.githubusercontent.com/musedata/humdrum-haydn-quartets/master/kern/op76n3-02.krn"
AddRaw 'haydn-op76n3' 'op76n3-03.krn' "https://raw.githubusercontent.com/musedata/humdrum-haydn-quartets/master/kern/op76n3-03.krn"
AddRaw 'haydn-op76n3' 'op76n3-open-score.mxl' ($SQ + "scores/Haydn,_Joseph/String_Quartet_in_C_major,_Hob.III77,_Op.76_No.3/sq20428156.mxl")

foreach ($m in @('a','b','c','d')) {
  AddRaw 'haydn-sym104' ("sym104" + $m + ".krn") ("https://raw.githubusercontent.com/musedata/humdrum-haydn-symphonies/master/kern/sym104" + $m + ".krn")
}

AddRaw 'haydn-seven-last-words' 'haydn-op51-seven-last-words.mxl' ($SQ + "scores/Haydn,_Joseph/Die_Worte_des_Erlösers_am_Kreuze,_Hob.III50–56,_Op.51/sq19815031.mxl")
AddRaw 'mozart-k421'   'mozart-k421.mxl'   ($SQ + "scores/Mozart,_Wolfgang_Amadeus/String_Quartet_No.15_in_D_minor,_K.421417b_(Op._10,_No._2)/sq7294793.mxl")
AddRaw 'schubert-d810' 'schubert-d810.mxl' ($SQ + "scores/Schubert,_Franz/String_Quartet_in_D_minor,_D.810,_No.14_(" + [char]0x201C + "Death_and_the_Maiden" + [char]0x201D + ")/sq7397765.mxl")
AddRaw 'brahms-op51n1' 'brahms-op51n1.mxl' ($SQ + "scores/Brahms,_Johannes/String_Quartet_No.1,_Op.51_No.1/sq7108150.mxl")
AddRaw 'smetana-sq1'   'smetana-sq1-from-my-life.mxl' ($SQ + "scores/Smetana,_Bedřich/String_Quartet_No.1/sq7483523.mxl")
AddRaw 'dvorak-op96'   'dvorak-op96-american.mxl' ($SQ + "scores/Dvořák,_Antonín/String_Quartet_No.12,_Op.96_(" + [char]0x201C + "American" + [char]0x201D + ")/sq8885439.mxl")
AddRaw 'debussy-quartet' 'debussy-op10.mxl' ($SQ + "scores/Debussy,_Claude/String_Quartet_in_G_minor,_Op.10/sq8661306.mxl")

AddRaw 'schubert-lieder' 'D957-04-Standchen.mxl'  ($LD + "scores/Schubert,_Franz/Schwanengesang,_D.957/04_Ständchen/lc5004835.mxl")
AddRaw 'schubert-lieder' 'D911-01-Gute-Nacht.mxl' ($LD + "scores/Schubert,_Franz/Winterreise,_D.911/01_Gute_Nacht/lc5015378.mxl")
AddRaw 'schubert-lieder' 'D911-05-Der-Lindenbaum.mxl' ($LD + "scores/Schubert,_Franz/Winterreise,_D.911/05_Der_Lindenbaum/lc5016466.mxl")

AddRaw 'brahms-op91' 'op91-1-Gestillte-Sehnsucht.mxl' ($LD + "scores/Brahms,_Johannes/2_Gesänge,_Op.91/1_Gestillte_Sehnsucht/lc6302395.mxl")
AddRaw 'brahms-op91' 'op91-2-Geistliches-Wiegenlied.mxl' ($LD + "scores/Brahms,_Johannes/2_Gesänge,_Op.91/2_Geistliches_Wiegenlied/lc6320420.mxl")

$ari = @(
  @{n="1_C’est_l’extase_langoureuse"; out="ariettes-1-Cest-lextase.mxl"; id="lc5060910"},
  @{n="2_Il_pleure_dans_mon_coeur";  out="ariettes-2-Il-pleure.mxl";    id="lc5060918"},
  @{n="3_L’ombre_des_arbres";        out="ariettes-3-Lombre-des-arbres.mxl"; id="lc5060924"},
  @{n="4_Paysages_belges._Chevaux_de_bois"; out="ariettes-4-Paysages-belges.mxl"; id="lc5060932"},
  @{n="5_Aquarelles_I._Green";       out="ariettes-5-Green.mxl";        id="lc5060938"},
  @{n="6_Aquarelles_II._Spleen";     out="ariettes-6-Spleen.mxl";       id="lc5060943"}
)
foreach ($a in $ari) { AddRaw 'debussy-ariettes' $a.out ($LD + "scores/Debussy,_Claude/Ariettes_Oubliées/" + $a.n + "/" + $a.id + ".mxl") }

$dh = @(
  @{n="01_Im_wunderschönen_Monat_Mai"; id="lc4976777"}, @{n="02_Aus_meinen_Tränen_sprießen"; id="lc4976769"},
  @{n="03_Die_Rose,_die_Lilie"; id="lc4976849"}, @{n="04_Wenn_ich_in_deine_Augen_seh’"; id="lc4978368"},
  @{n="05_Ich_will_meine_Seele_tauchen"; id="lc4978373"}, @{n="06_Im_Rhein,_im_heiligen_Strome"; id="lc4978379"},
  @{n="07_Ich_grolle_nicht"; id="lc4978382"}, @{n="08_Und_wüssten’s_die_Blumen"; id="lc4978387"},
  @{n="09_Das_ist_ein_Flöten_und_Geigen"; id="lc4978390"}, @{n="10_Hör’_ich_das_Liedchen_klingen"; id="lc5003150"},
  @{n="11_Ein_Jüngling_liebt_ein_Mädchen"; id="lc4978393"}, @{n="12_Am_leuchtenden_Sommermorgen"; id="lc4978395"},
  @{n="13_Ich_hab’_im_Traum_geweinet"; id="lc4978396"}, @{n="14_Allnächtlich_im_Traume"; id="lc4978397"},
  @{n="15_Aus_alten_Märchen_winkt_es"; id="lc4978398"}, @{n="16_Die_alten,_bösen_Lieder"; id="lc4978400"}
)
foreach ($d in $dh) {
  $safe = ($d.n -replace ("[ ,’]"), '-')
  AddRaw 'schumann-dichterliebe' ("op48-" + $safe + ".mxl") ($LD + "scores/Schumann,_Robert/Dichterliebe,_Op.48/" + $d.n + "/" + $d.id + ".mxl")
}

$log = @()
foreach ($it in $items) {
  $dir = Join-Path $root $it.slug
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $out = Join-Path $dir $it.name
  $u = if ($it.raw) { RawUrl $it.raw } else { $it.url }
  if (Test-Path $out) { Remove-Item $out -Force }
  $errf = $out + '.err'
  $cargs = @('-sS','-L','--max-time','180','--fail','-A','music-wiki-source-assistant/1.0','-o',$out,$u)
  Start-Process -FilePath 'curl.exe' -ArgumentList $cargs -NoNewWindow -Wait -RedirectStandardError $errf | Out-Null
  $size = if (Test-Path $out) { (Get-Item $out).Length } else { 0 }
  $ok = if ($size -gt 0) { 'OK' } else { 'FAIL' }
  $log += ("{0,-24} {1,-40} {2,-5} {3,9:N0}" -f $it.slug, $it.name, $ok, $size)
  if ($size -eq 0) {
    if (Test-Path $errf) { $log += ("    err: " + ((Get-Content $errf -Raw) -replace "`r?`n",' ') + "  url=" + $u) }
  }
  if (Test-Path $errf) { Remove-Item $errf -Force }
}
$log | ForEach-Object { Write-Output $_ }
Write-Output "==== SUMMARY ===="
Get-ChildItem $root -Recurse -File | Where-Object { $_.Name -ne '来源与许可.md' } | Group-Object { $_.Directory.Name } | Sort-Object Name | ForEach-Object {
  "{0,-24} files={1,-3} bytes={2,10:N0}" -f $_.Name, $_.Count, (($_.Group | Measure-Object Length -Sum).Sum)
}



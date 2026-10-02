# skein.nexus change plan (2026-10-01 night)

Site: `skein-nexus/site-v2` (parts/l1-overview.html, l2-pillars.html, l2-uses.html, l3-tech.html → build.py → index.html → dist/).
Compared against: skein main **063d30b**, log format **8** (#77 merged), the #31 tracker (State line, the three "Decided 2026-10-01 (afternoon)" sections, "Parked … parallel steps", "Discussed … storage hierarchy"), #77 (build comment, close comment, eleven "David to review" calls), #78, #79, #80, #39, #11; docs/APPS.md, MESSAGES.md, VM.md, BOOTSTRAP.md, kernel-zig/README.md, README.md. Where ARCH.md / WALLET.md / README.md disagree with MESSAGES/VM/APPS, the latter win (#80 is the sweep).

The earlier audit (nexus-audit-1.md) was re-checked item by item; every "now false" item there is still false on the site, and #77 adds more: routes, subscriptions, the `subscribe` import and the head/objects/subscribe handler programs are gone; the dispatch table, the four tables and write-scope-by-name replace them.

Tags: **built** = on main with tests. **decided-not-built (#nn)** = decided with David, not on main. **remove** = take out; nothing replaces it. Badges use the site's existing classes: `built`, `wip` (in progress), plain (`designed`, `not yet`). The plan adds one badge word, **not decided**, as a plain status. "designed" on the site = decided-not-built.

Vocabulary used in all the proposed wording: no "router"; **host** = transports + providers + store + oracle; the kernel's **dispatch table** routes; **oracle**, not "signer"; **write cache**, not "scratch space"; **overlay services** = the BRC-22 tools; an overlay is an app.

---

## 1. Overview — "A computer with its own keys and a complete memory." (l1-overview.html, L1–132)

### (a) Still right, stays
- Hero h1 and lede (L5–6). The diagram (L10–83) and its caption (L85): the one door, the sandbox with no disk/network/clock, the graph with heads. Keys drawn at the door is still fair: keys stay outside with the oracle, and everything that crosses is signed.
- Sandbox pillar (L92–97) and Graph pillar (L104–109).
- The three "together" lines (L112–116). "If something reached the skein, it came through the door, so it's in the graph" is now *more* true (every package is appended, #68).
- Use cards: agents (L122), identity (L123), your work (L125), bitcoin (L126), deploy (L127).

### (b) Changes
1. **L101** (Keys pillar), **built** — MESSAGES.md "The providers"; VM.md "emit"
   - now: "Messages come in signed by their sender, Bitcoin data comes with its proof, and anything the skein asks the outside world for comes back signed by the host that fetched it."
   - proposed: "Messages come in signed by their sender, Bitcoin data comes with its proof, and anything the skein asks the outside world for comes back as a signed message from the service that fetched it."
2. **L124** (network card), **remove** "pay"; payments between skeins are #11, not decided
   - now: "Skeins message and pay each other the same way you message them, and every exchange is signed and kept."
   - proposed: "Skeins message each other the same way you message them, and every exchange is signed and kept."
3. **L131** (status legend), **built** (wording only)
   - now: "Pages mark each part as built, in progress or designed."
   - proposed: "Pages mark each part as built, in progress, designed (decided, not built yet) or not decided."

### (c) Badges
- Legend gets the fourth word (above). No badges otherwise on this page.

### (d) New
- One sentence after the pillars (a new short `<p class="quiet">` under L116, or appended to the Sandbox pillar), **built** (APPS.md §1, §3; #31 "everything else is an app"):
  "What a skein does depends on the apps its owner installs: a shell, a wallet, an overlay, a website. Each app is a tree of programs installed under its own name, and writes only there."

---

## 2. The sandbox — "The sandbox: a computer with no side doors" (l2-pillars.html, L3–54)

### (a) Still right, stays
- Lede (L6). "What runs inside" (L9–10, built). The userland list (L13–16). Swap rows Disk, Clock, Randomness, Other processes (L24, L26–28). Fuel (L33–34, built). "Where the sandbox runs" (L40–41, built). Go-deeper cards (L46–52).

### (b) Changes
1. **L11**, **built** — BOOTSTRAP.md "Installing an app" (workbench row), #31 State item (a)
   - now: "Each skein comes with a working userland:"
   - proposed: "The stock system comes with a working userland:"
   - (The shell is the kernel's own pinned program; run and the chat loop come from shruggr/skein-workbench and are wired by the stock genesis. Whether the workbench becomes an installed app is open for David, #31 "For David (a)": do not say either way.)
2. **L25** (swap row "The network"), **built** — VM.md "emit"; MESSAGES.md "Outbound"
   - now: "Nothing direct. To reach outside it sends a message or makes a request, and the request and its answer are written into the history."
   - proposed: "Nothing direct. To reach outside, a program sends a signed message and waits. The answer arrives as a new entry in the history and wakes it again."
3. **L37**, **built** — VM.md "emit" (the oracle is the one recorded call)
   - now: "A step's inputs are all in the history: the message that woke it, the files it saw, the answers to anything it asked for."
   - proposed: "A step's inputs are all in the history: the entry that woke it, the files it saw, and the signatures it asked for."
4. **L38**, tone, **built** — kernel-zig/README.md "Equivalence"
   - now: "This is tested, not claimed: the test suite replays every stored history into a fresh store, twice, natively and in headless Chrome, and requires identical results."
   - proposed: "The test suite replays every stored history into a fresh store, twice, natively and in headless Chrome, and requires identical results."
5. **L43**, tone
   - now: "<b>Honest limits today.</b>"
   - proposed: "<b>Limits today.</b>" (rest of the note stays: still true.)

### (c) Badges
- No change; the four `built` badges stay true.

### (d) New
- Nothing.

---

## 3. Keys and the door — "Keys and the door" (l2-pillars.html, L57–108)

### (a) Still right, stays
- Lede (L60). "An identity of its own" (L63–64, built). L68 ("Where the keys actually live is up to whoever runs the skein…"). Door rows: A message (L79), A payment (L80), Block headers and proofs (L81), A peer-to-peer message (L82). "Why this matters" (L91–96).

### (b) Changes
1. **L67**, **built** — WALLET.md "The builder and the oracle"; VM.md "Programs and execution"
   - now: "Signing is a request to a separate signer outside the sandbox, which sees a reference to a key and a 32-byte hash and nothing else. Each request and the signature that came back are written into the history, and signatures are deterministic, so replay matches exactly."
   - proposed: "Signing is a request to the oracle, a separate service outside the sandbox, which sees a reference to a key and a 32-byte hash and nothing else. Each request and the signature that came back are written into the history, and signatures are deterministic, so replay matches exactly."
2. **L71**, **built** + **decided-not-built (#78)** — WALLET.md "Pieces"; #78
   - now: "Its coins, transactions, proofs and block headers are records in the graph like everything else. It builds and signs transactions (through the signer) and checks incoming payments against their proofs before it accepts them."
   - proposed: "Its coins and transactions are records in the graph like everything else. It builds and signs transactions (through the oracle) and checks incoming payments against their proofs before it accepts them. <span built>built</span> The headers, proofs and transaction status are moving to one chain app that the wallet and every overlay read. <span designed>designed</span>"
3. **L76**, **built** — MESSAGES.md "The persistence rule", "The instance as an HTTP server"
   - now: "Every skein is a small web server at its own address. Each request goes through one program, the front door, which runs mutual authentication (BRC-103/104) and decides what gets written."
   - proposed: "Every skein is a small web server at its own address. Each request is written to its history as it arrived, and one program, the front door, runs on it: it checks mutual authentication (BRC-103/104), and the skein's dispatch table decides which program gets what it carries."
4. **L83** (door row "Something the skein asked for"), **built**; badge `designed` → `built` — MESSAGES.md "The providers"; #67, #70
   - now: "A web request goes out through a proxy the host provides, which signs the request and the answer it got. Both are written on the step that made them, so the step replays."
   - proposed: "The skein sends a signed message to a provider (for a web request, the host's HTTP proxy) and waits. The answer is a signed message from the provider, written as its own entry, so the step that reads it replays."
5. **L88–89** (section "Only state gets written"), **built**; heading and text change — MESSAGES.md "The persistence rule (#68)"
   - now (h2): "Only state gets written"
   - proposed (h2): "Everything that arrives is written"
   - now: "Reads, polls and handshakes leave no trace. A message that arrives is one record; checking your inbox ten thousand times writes nothing (that’s a test). A record is written only when the state actually changes."
   - proposed: "Every request that reaches the skein is written as it arrived, reads and handshakes included, the way a web server keeps an access log. A read changes nothing else. A handshake writes the session, so it survives a restart. How long old reads are kept is a pruning question."
6. **L104–105** (go-deeper cards), **built**
   - "The front door, sessions, routes, mailboxes, libp2p." → "The front door, sessions, the dispatch table, mailboxes, libp2p."
   - "The signer, SPV, settlement, overlay nodes." → "The oracle, SPV, settlement, overlays."

### (c) Badges
- L83 row: `designed` → `built`.
- L71: add `designed` on the chain-app sentence (#78).

### (d) New
- One new door row after L83, **built** (MESSAGES.md "Broadcast out, proofs and statuses in"):
  "**A transaction's status** | Optional. Signed by a status provider the skein chose to listen to. Without one, the skein learns a transaction is in by its proof arriving. `built`"

---

## 4. The graph — "The graph: history you can branch" (l2-pillars.html, L111–210)

### (a) Still right, stays
- Lede (L114). "Named by content" (L117–119, built). "Searchable by how things connect" (L133–135, both badges). The diagram (L139–175). "Heads, branches and merges" (L179–181). The three levels (L186–190). "Why this matters" (L194–199).

### (b) Changes
1. **L125**, **built** — VM.md "emit" (only the oracle's answers are on a step)
   - now: "<b>Steps</b> programs took, with the work they cost and the answers to anything they asked for."
   - proposed: "<b>Steps</b> programs took, with the work they cost and the signatures they asked for. Answers from outside are entries of their own."

### (c) Badges
- None change.

### (d) New
1. Add to the "What's in it" list (after L126), **built** (VM.md "The dispatch table, and the kernel's four tables"):
   "<b>The skein's own tables</b>: which program each kind of message goes to (the dispatch table) and how to reach each key it knows (the address book), each a chain of changes like everything else."
2. Add to "Heads, branches and merges" (after L181), **built** (APPS.md §1; VM.md "Heads"):
   "Every head has an owner: the app whose name it starts with (<code>overlay/…</code>, <code>wallet/…</code>). An app can move only its own heads. Any program can read any record whose hash it holds."

---

## 5. Watch a model work, turn by turn (l2-uses.html, L3–79)

### (a) Still right, stays
- All of it. The loop emits to the inference peer and the completion comes back as a signed reply (MESSAGES.md "The infer protocol"); context deltas are built; the note at L69 is right.

### (b) Changes
- None required.

### (c) Badges
- None.

### (d) New
- Optional, **built**: after L11, "The conversation loop and the shell come from the workbench app (shruggr/skein-workbench)." Only if David wants app names on l2.

---

## 6. Give every agent, and every person, a skein (l2-uses.html, L82–115)

### (a) Still right, stays
- Lede (L85). "A person's skein" (L91–92, built: mailbox instances, `POST /account/register`). "Finding each other" (L94–95, built).

### (b) Changes
1. **L89**, **built** — MESSAGES.md "The dispatch table and the kernel's operations"
   - now: "Anyone who knows its key can message it; whether it answers depends on what it has subscribed to."
   - proposed: "Anyone who knows its key can message it; whether it answers depends on its dispatch table, which says which senders may reach which program."
2. **L99** label, **built**
   - now: "Running today"
   - proposed: "Running in development"
3. **L101**, **built**
   - now: "Martha and Kurt, two bopen.ai personalities, each in their own skein. They chat with people and consult each other, and each keeps its own side of the conversation."
   - proposed: "Martha and Kurt, two bopen.ai personalities, each in their own skein on a development host. They chat with people and consult each other, and each keeps its own side of the conversation. Nothing is publicly hosted yet."
4. **L103**, **built**
   - now: "…on the browser build of the kernel, with your wallet as its signer."
   - proposed: "…on the browser build of the kernel, with your wallet as its oracle."
5. **L102** (chat front end): verify with David. #31 says the bopen-skein manual Yours checklist is untried, and every dev store was re-genesised for format 8. If it hasn't been run since #77, say "being updated" or drop the row.

### (c) Badges
- None change.

### (d) New
- Nothing.

---

## 7. Let skeins work with each other, in the open (l2-uses.html, L118–148)

### (a) Still right, stays
- Lede (L121). "One way of talking" (L124–126, built: replies route only from the key the message went to).

### (b) Changes
1. **L129** (Broadcast, too), **built** — MESSAGES.md "libp2p (#51)"
   - now: "A message accepted from a topic is written as a record that re-verifies from its publisher’s signature; a duplicate or rejected one writes nothing."
   - proposed: "A message accepted from a topic is written as a record that re-verifies from its publisher’s signature. A rejected or repeated one is recorded as refused, and nothing runs."
2. **L132** (Shared Bitcoin services), **built** — APPS.md §6; #72 close; #74; #31 "@bsv/sdk overlay clients are wrong"
   - now: "A skein can act as an overlay node: it accepts transactions for a topic, keeps the ones its rules admit, and answers lookups about them, using the standard BSV client libraries. If no topic admits a transaction, nothing is stored. One application is being built on this now: an automated market maker, where validators run as skeins."
   - proposed: "An overlay is an app: the overlay engine plus your own topic managers and lookup services, installed under one name. It takes transactions for its topics at <code>/&lt;handle&gt;/&lt;app&gt;/submit</code>, keeps the ones its rules admit, answers lookups, and shares what it admitted with peers over libp2p. If no topic admits a transaction, only the request is recorded. `built` An automated market maker is being prototyped on it, with validators running as skeins."
   - Check the AMM sentence with David (amm-poc is his other session; earlier audit could not verify "being built").
3. **L134–135** (Paying each other), **remove** the plan sentence; badge `designed` → `not decided` — #11 open; #31 "Open for later walkthroughs: #11 payments"
   - now: "The plan is that tolls and quotes ride on the messages, and each program sets its own spending policy. A skein that has money could pay another for work, or pay to start a new one."
   - proposed: "A skein’s wallet can receive a payment and make a transaction today. `built` How skeins quote, charge and pay each other for work is not decided. `not decided`"
4. **L137** (note), tone
   - now: "<b>Why the record matters here most.</b> Programs that can message and pay each other are powerful, and it’s reasonable to be uneasy about that. Skein’s answer isn’t to forbid it but to make it inspectable: every message between them is signed, every step is kept, and any step can be re-run."
   - proposed: "<b>Why the record matters here.</b> Programs that message each other and hold money should be inspectable. Every message between them is signed, every step is kept, and any step can be re-run."
5. **L145** (card), **built**: "Topic managers and lookup services on hashes." → "Overlays as apps: topic managers and lookup services."

### (c) Badges
- L135 `designed` → `not decided` (plus a `built` for the wallet sentence).

### (d) New
- Nothing beyond the overlay rewrite.

---

## 8. One graph over all your work (l2-uses.html, L151–178)

### (a) Still right, stays
- All of it. The note at L168 is still accurate.

### (b) Changes
- None. (Optional: workbench#1, the shell's `mount`, is filed but not built, so don't mention it.)

### (c)/(d)
- None.

---

## 9. Your own slice of Bitcoin, indexed and proven (l2-uses.html, L181–210)

### (a) Still right, stays
- Lede (L184). "What it holds" (L187–189, built; Chronicle). "Settlement you can read" (L191–192, built). "Walk it" (L194–195: the explorer is the front door's `/explore` route, read op `explore`, owner only; built).

### (b) Changes
1. **L198**, **remove** the last sentence (undecided economics, tone)
   - now: "Your records don’t depend on a service staying up or staying honest. The proofs travel with the data. The cost of indexing is paid by whoever wants the index, which is how the overlay ecosystem can pay for itself."
   - proposed: "Your records don’t depend on a service staying up or staying honest. The proofs travel with the data."
2. **L199**, **built** — MESSAGES.md "Broadcast out, proofs and statuses in"; WALLET.md "Broadcasts, proofs and statuses"
   - now: "Not built yet: catching up on headers after a gap, and fetching proofs on demand. Feeds deliver headers and transaction status as they happen."
   - proposed: "Headers arrive from a feed the host follows, and a transaction’s proof comes back from the host’s broadcaster; both check themselves against the chain. Statuses come only from a status provider the skein chose to listen to. Not built yet: catching up on headers after a gap, and fetching proofs on demand."

### (c) Badges
- Add `designed` to the new chain sentence (d).

### (d) New
- After L188, **decided-not-built (#78)**: "One app per skein keeps this chain state, the chain app. The wallet and every overlay read it rather than keeping copies. `designed`"

---

## 10. Start from a commit, run anywhere (l2-uses.html, L213–243)

### (a) Still right, stays
- Lede (L216). "Where the tree comes from" list (L223–227). "Same skein, different machines" (L230–231, built). The note at L233.

### (b) Changes
1. **L220**, **built** — BOOTSTRAP.md "The system tree"; VM.md "The dispatch table"
   - now: "Programs live in <code>bin/</code> as WebAssembly, and configuration lives in <code>etc/</code>: who may send what to which program, which web routes exist, and which Bitcoin feeds to follow."
   - proposed: "Programs live in <code>bin/</code> as WebAssembly, and configuration lives in <code>etc/</code>: the dispatch table’s first rows (which sender may reach which program, by message box, web path or peer-to-peer topic) and which Bitcoin feeds to follow."
2. **L228**, tone
   - now: "When the code comes from the chain, who published it and which version ran are both part of the record. You get code signing without doing anything extra."
   - proposed: "When the code comes from the chain, who published it and which version ran are both part of the record."
3. **L240** (card), **built**: "System trees, packets, checkpoints, re-genesis." → "System trees, apps, packets, checkpoints."

### (c) Badges
- None change.

### (d) New
- After L220, **built** (APPS.md §3; BOOTSTRAP.md "Installing an app") + **not decided** (bundles; #31 "Discussed… storage hierarchy", "bare genesis + bundles"):
  "Apps go in afterwards. Each app is its own repository, and the owner installs it into a running skein. The install shows the rows the app asks for and sends them only once the owner approves. `built` Every genesis already carries the owner’s admin rows. Starting from a bare genesis and adding a ready-made bundle of apps is the direction; what a bundle is has not been decided. `not decided`"

---

## 11. Hosting, cost, and getting one (l2-uses.html, L246–289)

### (a) Still right, stays
- Lede first sentence (L249: "A skein needs a host to keep it reachable, and it costs something to run."). "There’s no public hosting yet." (L254). Cost table (L259–263) and "No prices are set yet." (L264).

### (b) Changes
1. **L249** second sentence, **remove** — #39/#11 not decided (see note)
   - now: "The plan is that each skein pays its own way from its own wallet."
   - proposed: drop it.
2. **L253** ("What a host does"), **built** — VM.md "The dispatch table…" ("The host (transports + providers + store + oracle) routes nothing"); MESSAGES.md "The providers"; kernel-zig/README.md "How serve is put together"
   - now: "Whatever it is, it does the same few jobs: routes requests to the right skein, provides signing outside the sandbox, makes outside requests on the skein’s behalf, follows Bitcoin feeds, wakes sleeping tasks on time, and connects to peer-to-peer networks. It makes no decisions. Everything that matters happens inside the skein, so a skein can move between hosts."
   - proposed: "Whatever it is, it does the same few jobs. It carries what arrives (web requests, peer-to-peer messages) into the right skein’s history. It answers signing requests through the oracle, outside the sandbox. It carries out the messages a skein sends, through its providers: an HTTP proxy, a waker, a cron service, a libp2p node, and optionally a transaction-status service. It broadcasts transactions, brings back headers and proofs, and keeps the store. It decides nothing and routes nothing inside: the skein’s own dispatch table does that. So a skein can move between hosts."
3. **L268–269** ("How it would pay"), badge `designed` → `not decided`; **remove** the mechanism — #39, #11; #31 "Open for later walkthroughs: #11 payments / deploy-by-message / billing"
   - now (h2): "How it would pay <span>designed</span>"; body: the payment-channel paragraph.
   - proposed (h2): "How it pays <span>not decided</span>"; body: "Fuel is already counted per step, so the bill can be worked out from the history. How a skein pays its host is not decided. One option under discussion is a payment channel from the skein’s own wallet to its host."
   - **Flag for David:** #39’s body has a “Decided 2026-09-28” section on billing and the stand-up flow. Since then, the 10-01 tracker lists billing as open, and bare genesis + bundles replace “starts from the initial state we deploy”. The brief says not decided, so the plan follows that, but #39 should be reconciled.
4. **L271–279** ("Getting one"), badge `designed` → `not decided`; **remove** the four steps and L279 — #39; BOOTSTRAP.md "Commands"
   - proposed (h2): "Getting one <span>not decided</span>"; body: "Today whoever runs a host starts a skein for an owner key, and the owner installs apps into it. How you would ask someone else’s host for a skein, and pay for it, is not decided."
   - L279 "skein.nexus is meant to become the page where you connect your wallet and see and manage the skeins you control." → **remove** (#39 is open; this page is information only).
5. **L286** (card), **built**: "Built, in progress, designed." → "Built, in progress, designed, not decided."

### (c) Badges
- Both section badges `designed` → `not decided`. Keep `built` on "What a host does" and `metered` on Computation.

### (d) New
- Nothing.

---

## 12. Architecture — "Architecture" (l3-tech.html, L3–86) — needs a rewrite

### (a) Still right, stays
- "The runtime judges nothing…" idea in the caption (L56), with "host" for "runtime" (below). Kernel paragraph core (L61: store, log, scheduler, WASI, wasmtime C API static, kernel-zig, wasm32-freestanding, CLI `serve | replay | shell | dump | fuel`). Program sizes: still roughly right (wasm/: 100 KB run-handler to 670 KB wallet). Write "about 100–670 KB" or keep "70–670 KB".

### (b) Changes
1. **L6** lede, **built** — #31 "the kernel is the machine, four tables and the oracle; everything else is an app"; VM.md
   - now: "A deterministic WASI machine over a content-addressed graph. It has three layers: one kernel, a catalogue of programs, and several runtimes that drive the kernel from outside."
   - proposed: "A deterministic WASI machine over a content-addressed graph. It has three layers: one kernel (the machine, four tables and the oracle), the apps and programs that run on it, and the hosts that drive it from outside."
   - Vocabulary note: #31’s 09-30 layer decision says “runtimes”; the 10-01 docs say “host”. The plan uses “host” throughout l3, per the vocabulary rule. David to confirm.
2. **L9 + SVG L17–53** (diagram), **built**; redraw:
   - Host bar title (L18): "runtime (host): a server · a desktop · a browser tab" → "host: a server · a desktop · a browser tab".
   - Host boxes (L20–26) "routing · signer · feeds · libp2p host · waker · fuel ledger · http proxy" → "transports (http · libp2p)" · "oracle" · "providers (fetch · waker · cron · libp2p · status)" · "broadcaster + feeds" · "store" · "fuel ledger". No "routing" box (vocabulary).
   - Contract label (L30) "frames: admit · call · wallet · http · libp2p" → "frames: admit · answer · call in — wallet · emit out".
   - Kernel title (L33) "kernel: one per instance (Zig + wasmtime)" stays; add a row of four small boxes: "objects · heads · dispatch · address book".
   - Programs box (L35–44): drop "run · objects · head · subscribe" (objects/head/subscribe handlers deleted in #77). Two groups: "boundary programs: front door · messagebox · resolve · wallet" and "apps: workbench (shell · git · qjs · python · run · loop) · overlay · static · chain*" (*#78, mark designed or leave out until merged).
   - Store box (L47–52) stays.
   - aria-label (L9): reword the same way ("a host provides transports, an oracle, providers, feeds, a broadcaster and a fuel ledger… each kernel holds four tables and runs boundary programs and apps").
3. **L56** caption, **built**
   - now: "The runtime judges nothing. Everything that matters is decided by programs inside the kernel and written to the store."
   - proposed: "The host judges nothing and routes nothing. The kernel’s dispatch table routes, and everything that matters is decided by programs inside the kernel and written to the store."
4. **L61** (Kernel), **built** — kernel-zig/README.md intro; VM.md
   - add after the first sentence: "It keeps four tables: objects (blocks by hash), heads (each with an owner), the dispatch table, and the address book. The owner’s admin messages change them, and the kernel does that itself; no program can."
5. **L64** (Programs and the SDK), **built** — #77 build comment; BOOTSTRAP.md "Installing an app"; README.md layout
   - now: "A catalogue, not a fixed set: front door, messagebox, wallet, resolve, overlay, fetch, p2p, the workbench programs (<code>run</code>, <code>objects</code>, <code>head</code>, <code>subscribe</code>, <code>loop</code>) and the SDK they’re written against. Each genesis wires its own subset; none is mandatory. The stock programs are Zig, 70–670 KB each."
   - proposed (h2 → "Programs, apps and the SDK"): "Two kinds. The boundary programs live in skein’s repository: the front door, the messagebox, resolve and the wallet. Everything else is an app in its own repository, installed under its own name: the workbench (the shell and its tools, <code>run</code>, the chat loop), static files, the overlay engine, and the chain app (#78, being built). All are written against skein-sdk, a Zig package (v0.3.0). The stock programs are Zig, 100–670 KB each."
   - fetch and p2p are no longer programs: fetch is a host provider, and p2p is a test fixture (programs/test).
6. **L66–67** (Runtimes), **built**; h2 "Runtimes" → "Hosts"
   - now: "Whatever drives a kernel from outside. A runtime implements one contract: admitting entries, making calls, giving the kernel a store, and answering its outbound requests (signing, HTTP, libp2p). How it holds keys, where it stores bytes and how it’s deployed are its own business. Today there’s a server runtime and a browser runtime, and the same history replays under either."
   - proposed: "Whatever drives a kernel from outside: transports, providers, a store and an oracle. A host appends what its transports carry in, waits for a request’s answer, answers the oracle’s signing requests, and carries out what the skein emits through its providers. How it holds keys, where it stores bytes and how it’s deployed are its own business. Today there’s a server host and a browser host, and the same history replays under either."
7. **L69–76** (The kernel’s whole surface) — table rewrite; see §Structure. **built** — kernel-zig/README.md "How serve is put together", "Requests and answer", "Calls"
   - `admit`: "The one call in that writes: append a log entry, then run the steps it drives." → "The one call in that writes: append a package as it arrived, then run the steps it drives."
   - **new** `answer`: "Wait until a request’s thread comes to rest, and return its answer. This is how a waiting web client gets its reply."
   - `call` (L72): "Run a program function over current state. No entry, no writes, not replayed; its fuel goes to the host’s ledger. Every web read is one of these." → "Run a program function over current state. No entry, no writes, not replayed; its fuel goes to the host’s ledger. Only for host-side reads that are not requests, such as the explorer’s pages."
   - `wallet` (L73): "Out: key operations, answered by the runtime’s signer." → "Out: key operations, answered by the host’s oracle. The one call recorded on the step."
   - **new** `emit`: "Out: committed messages for providers and libp2p peers, and broadcast transactions, carried by the host after the step ends."
   - `http` (L74), `libp2p` (L75) → **remove** (format 6 removed both imports).

### (c) Badges
- None on the page. Optionally add `designed` to the chain box in the diagram.

### (d) New
- Covered by 4, 5 and 6: the four tables, apps, and the dispatch table replacing routing.

---

## 13. Data model: git and Bitcoin in one graph (l3-tech.html, L89–187)

### (a) Still right, stays
- Lede; families table (L96–101); diagram; Git mapping (L164); Bitcoin mapping (L167); Edges (L177). The earlier audit's "t-data entirely" mostly holds.

### (b) Changes
1. **L98** (skein family), **built** — README.md "Records"
   - now: "Log entries, thread origins and updates, messages, index nodes, the state record."
   - proposed: "Log entries, thread origins and updates, messages, head updates (with their owner), dispatch-table changes, app records, index nodes, the state record."
2. **L170**, **built** — VM.md "The dispatch table"
   - now: "Threads, heads, subscriptions and the address book are all chains."
   - proposed: "Threads, heads, the dispatch table and the address book are all chains."
3. **L173** map list, **built** — VM.md "The index"
   - now: "<code>log</code>, <code>unique</code>, <code>chains</code>, <code>threads</code>, <code>resting</code>, <code>sleepers</code>, <code>awaits</code>, <code>edges</code>, <code>heads</code>."
   - proposed: add <code>updates</code> after <code>chains</code>. (`sleepers` stays: a derived read since format 7.)
4. **L174**, **decided-not-built** (retention, decided in the 10-01 rework, no issue yet)
   - now: "Pruning old index history is designed, not built."
   - proposed: "A store may forget what no head reaches and the log before its last checkpoint; no store prunes yet."
5. **L167** (proofs map), **decided-not-built (#78)**: add at the end: "Today the wallet keeps this map. With the chain app (#78) it moves under <code>chain/</code>, one copy for the whole skein."
6. Diagram L148 "state · step · calls · fuel" → optional "state · step · emitted · fuel". The update still has `calls` (the oracle), so either is true.

### (c)/(d)
- Nothing else. Do **not** mention the storage scope map (undecided).

---

## 14. The kernel and VM (l3-tech.html, L190–237)

### (a) Still right, stays
- Lede; ABIs (L197); Randomness (L210, with one word changed); Fuel (L213); Userland (L219–224); Browser build (L227: preview1 only, no libp2p; still true per ARCH "The browser as a host").

### (b) Changes
1. **L200–204** (syscall table) — rewrite; see §Structure. **built** — VM.md "Programs and execution", "emit"; #31 "Kernel-call inventory"
   - `Pure` row stays.
   - `Recorded` (L202): "<code>wallet</code>, <code>http</code>, <code>libp2p</code>. The request and answer are written on the step’s update; replay serves them from there, and a request that differs on replay is a divergence." → "<code>wallet</code> only: the oracle. The request and answer are written as an <code>oracle</code> record of the step; replay serves them from there, and a request that differs on replay is a divergence."
   - `Graph` (L203): "<code>get</code>/<code>put</code>/<code>putblock</code> by CID, <code>keep</code>, <code>launch</code>, <code>await</code>, <code>advance</code> (heads), <code>subscribe</code>, <code>deadline</code>, <code>edges</code>, <code>call</code>." → split into three rows:
     - **Reads**: "<code>input</code>, <code>get</code> by CID, <code>head</code>, <code>edges</code>. Global: any program reads any record it holds the CID of."
     - **Writes**: "<code>put</code>, <code>putblock</code>, <code>keep</code>, <code>advance</code>. <code>advance</code> only moves heads under the program’s own app name."
     - **Threads**: "<code>launch</code>, <code>await</code> (a record, a subject or another thread), <code>deadline</code>, <code>call</code>."
   - **new** row **Out**: "<code>emit</code>: a signed message to a key in the address book, or a broadcast transaction. Sent when the step ends; the answer is a new entry."
   - (`subscribe` removed in #77; `http`/`libp2p` removed in format 6.)
2. **L207** (Time), **built** — VM.md "deadline", "Scheduling"
   - now: "Sleep is a deadline; the waker admits one <code>wake</code> entry when it comes, and there are no periodic wake-ups."
   - proposed: "Sleep and deadlines are a message to the host’s waker, whose answer wakes the thread. A recurring job is a schedule a program sends to the cron provider. There are no wake entries."
3. **L210**, **built**: "so secrets are made by the signer instead" → "so secrets are made by the oracle instead".
4. **L213** (Fuel), **built**: "Kernel calls have their own limit (10<sup>10</sup>) and are charged to the host ledger." → "Kernel calls and the front door’s request steps have their own limit (10<sup>10</sup>); a kernel call’s fuel is charged to the host ledger."
5. **L216** (Replay), **built** — kernel-zig/README.md "Equivalence"
   - now: "The equivalence suite replays 16 real histories twice…"
   - proposed: "The equivalence suite replays 18 real histories twice…"

### (c)/(d)
- None beyond the table. Parallel steps are parked; do not mention them.

---

## 15. Messages and network (l3-tech.html, L240–285) — needs a rewrite

### (a) Still right, stays
- The origin forms (L247 first sentence), "The caller is the identity key the session proved; there are no accounts." The replyTo rule (L260 first sentence). Messagebox program (L264). Mailbox instances (L265). Inference protocol (L271). The libp2p peer-key sentence (L274 last).

### (b) Changes
1. **L243** lede, **built** — MESSAGES.md intro
   - now: "The instance is an HTTP server. BRC-103/104 is the network, BRC-33 is the mailbox, BRC-169 is discovery, and only messages are state."
   - proposed: "The instance is an HTTP server. BRC-103/104 is the network, BRC-33 is the mailbox, BRC-169 is discovery, and every package that arrives is written as received."
2. **L247**, **built** — MESSAGES.md "The instance as an HTTP server"
   - now: "The runtime forwards every request as one kernel <code>call</code> of the front-door program, which runs the BRC-103/104 handshake and verifies each message inside the VM. … Answers are signed on the session through the runtime’s signer."
   - proposed: "The host appends every request as received, and the kernel runs the front-door program on it as that request’s own thread: the BRC-103/104 handshake and the check of each message happen inside the VM. The host holds the client’s connection until the thread comes to rest. … Answers are signed on the session through the oracle."
3. **L248**, **built** — MESSAGES.md "Routes are rows of the dispatch table", "Route handlers"
   - now: "<code>etc/routes.json</code> maps paths to program functions (auth defaults to BRC-104; <code>"none"</code> is for open routes like overlay submit). <code>etc/reads.json</code> gates read routes by caller. A handler answers <code>{status, body, admit?, then?}</code>, and <code>admit</code> lists the entries to write."
   - proposed: "Routes are <code>http</code> rows of the dispatch table: a path or prefix, who may call it (<code>"session"</code> for any BRC-104 session, a key, or <code>"*"</code> for an open route like an overlay’s submit), and the program function to call. <code>etc/reads.json</code> gates read routes by caller. A handler answers <code>{status, type?, body, headers?, admit?}</code>; <code>{wait: true}</code> if the answer depends on a thread still running; or <code>{read: true}</code> for a live read. <code>admit</code> lists the messages and events to route."
4. **L251–257** (persistence table) — rewrite; see §Structure. **built** — MESSAGES.md "The persistence rule (#68)", "Sessions are state"
   - Message arrives: "One <code>mail</code> entry, carrying…" → "Its request, as received, is one entry. The front door’s step routes the <code>mail</code> record it carries; that record keeps the signed BRC-104 request, so authorship verifies from the log with keys alone."
   - Read or poll: "Nothing. Tested at 10,000 polls: 0 entries, 0 bytes." → "Its request entry, and nothing else moves. Growth is a pruning question."
   - Handshake: "Nothing. Sessions are held in memory, never in the log; after a restart the client simply handshakes again." → "Its request entry. The step writes the session under the head <code>frontdoor/sessions</code>, so sessions survive a restart (they expire after a day)."
   - Acknowledgement: "One entry: the reader’s pointer moves." → "Its request entry; the step admits an <code>:ack</code> event and the reader’s pointer moves."
   - Sending: "Part of the sending step: a recorded <code>http</code> call and the record it put. Not an entry." → "Part of the sending step: the signed message it emitted, listed on the update. Not an entry. The answer is an entry."
5. **L259–260** (Routing inside); h2 → "The dispatch table"; **built** — VM.md "The dispatch table"; MESSAGES.md "The dispatch table and the kernel's operations"
   - now: "Otherwise a message is routed by subscription on <code>(sender, box)</code>, first match wins. “A subscription is the permission”; the subscription table is itself a chain. No match means it’s recorded and nothing runs."
   - proposed: "Otherwise it is routed by the dispatch table: one table of rows (transport, address, sender, program) for message boxes, web paths and libp2p topics alike, first match wins. A row is the permission. The table is a chain that only the kernel writes, on admin messages from the owner or a delegate. No match means it’s recorded and nothing runs."
6. **L266** (Delivery), **built** — MESSAGES.md "The outbound BRC-103/104 pattern", "The address book"
   - now: "<code>send</code> looks up the address book (head <code>peers</code>: key → mailbox URL), reuses a BRC-104 session, and POSTs as a recorded call. Transient and permanent failures are distinguished; an unknown key is “no route”."
   - proposed: "An emitted message to a <code>mailbox</code> key is delivered by its own thread. The messagebox program acts as a BRC-103/104 client of the recipient’s messagebox, and each HTTP exchange is a message to the <code>fetch</code> provider. Its sessions are kept under the head <code>outbound</code>. The address book (head <code>peers</code>) maps key → transport (<code>mailbox</code>, <code>libp2p</code>, <code>local</code>) and address. Transient failures are retried; an unknown key is “no route”."
7. **L267** (Discovery), **built** — MESSAGES.md "BRC-169 is discovery"
   - now: "…manifest, then handle → identity key and messagebox, as recorded calls."
   - proposed: "…manifest, then handle → identity key and messagebox, each lookup a message to the <code>fetch</code> provider."
8. **L274** (libp2p), **built** — MESSAGES.md "libp2p (#51)"
   - now: "The runtime runs a libp2p node for each instance that asks for one (GossipSub with strict signing). Inbound arrives as front-door calls; an accepted topic message is one <code>p2p</code> entry that re-verifies from the log; duplicates and rejects write nothing. Outbound is the recorded <code>libp2p</code> import."
   - proposed: "The host runs a libp2p node (GossipSub with strict signing) for each instance whose dispatch table has libp2p rows, and follows the table live as apps are installed. Each topic message or stream frame is appended as a request and the front door judges it; an accepted message admits what a web submission would. A rejected or repeated one is a recorded refusal. Outbound is a message to the host’s libp2p provider: publish, dial, send, close."
9. **L275**, **built** — #57, #74
   - now: "Designed, not built: the front door forwarding admitted entries on every transport (today a transaction arriving by pubsub doesn’t persist overlay state the way <code>POST /submit</code> does)."
   - proposed: "A transaction submitted over pubsub persists exactly what <code>POST /submit</code> persists, and overlays gossip what they admitted and its proofs (<code>&lt;topic&gt;</code>, <code>-admit</code>, <code>-proof</code>)."
10. **L281–282** (cards), **built**: "The signer and what it signs." → "The oracle and what it signs."; "Where routes and subscriptions come from." → "Where the dispatch table’s rows come from."

### (c) Badges
- The page has none; nothing to change.

### (d) New
- New h2 after "Mailboxes, delivery, discovery": **"One way out: emit and the providers"**, **built** (VM.md "emit"; MESSAGES.md "The providers", "Scheduling", "Broadcast out…"):
  "A step never talks to the network. It emits a signed message to a key in the address book, ends waiting, and the answer is an entry that steps it again. The host’s providers are recipients with keys of their own: <code>fetch</code> (an HTTP proxy), <code>waker</code>, <code>cron</code>, <code>libp2p</code>, and an optional <code>status</code> provider. Each answers with a signed message. A broadcast is an unsigned event the host’s one broadcaster queues and retries; the proof comes back as an event. Whether a provider is local or remote is up to the address book."

---

## 16. Wallet and overlays (l3-tech.html, L288–321)

### (a) Still right, stays
- SPV and headers (L301). Settlement (L307). The core of the signer paragraph (L295), with words changed.

### (b) Changes
1. **L291** lede, **built** + **decided-not-built (#78, #79)** — #31 "the chain is its own head"; #78; #79
   - now: "The wallet is split in two: the keys stay outside with the runtime’s signer, and wallet state lives inside as records. The overlay node shares the same chain and settlement core."
   - proposed: "The wallet is split in two: the keys stay outside with the host’s oracle, and wallet state lives inside as records. Today the wallet and the overlay engine share one chain record. Being built: one chain app owns the chain state under <code>chain/</code>, and the wallet and each overlay keep their own records under their own names and read it."
2. **L294–295** (The signer), **built**: h2 "The signer" → "The oracle"; "requests to the runtime’s signer" → "requests to the host’s oracle"; "is the runtime’s business" → "is the host’s business".
3. **L298** (The wallet program), **built** — WALLET.md "Pieces"
   - now: "<code>wallet-zig</code> over bsvz, compiled to wasm."
   - proposed: "<code>programs/wallet</code>, built on the SDK’s wallet library over bsvz, compiled to wasm."
4. **L303–304** (Feeds), **built** + **decided-not-built (#78)** — MESSAGES.md "Broadcast out, proofs and statuses in"; #78
   - now: "The runtime holds subscriptions an instance declares (a header stream, and transaction status callbacks) and admits each item as a plain event entry. It judges nothing: headers and proofs validate themselves inside, and a broadcast status is provisional until there’s a proof."
   - proposed (h2 → "Broadcasts, proofs and statuses"): "Broadcasting is an emitted event; the host’s one broadcaster queues it and retries. Headers from a feed and proofs from the broadcaster come in as plain events and validate themselves inside. Statuses come only as signed messages from a status provider the instance has a row for, and stay provisional until there’s a proof. The host judges nothing. Being built (#78): the chain app is the one recipient of all three and the only thing that broadcasts; every unproven transaction it holds has a broadcast registered."
5. **L310** (Overlay node), **built**; h2 → "Overlays are apps" — APPS.md §6; #72; #74; #31
   - now: "An instance can serve BRC-22/24 through its own front door (<code>POST /submit</code>, <code>POST /lookup</code>, open auth). Submit decodes the BEEF once into records in the call’s scratch space, runs SPV, and asks topic managers <code>identify(tx: cid, …)</code>. … Tested against the stock <code>@bsv/sdk</code> broadcaster and resolver."
   - proposed: "An overlay is an app: the overlay engine (shruggr/skein-overlay) and its own topic managers and lookup services, installed under one name, with its wiring derived from <code>config.overlay</code> and shown to the owner at install. It serves BRC-22/24 at its base URL <code>/&lt;handle&gt;/&lt;app&gt;</code> (<code>/submit</code>, <code>/lookup</code>, open). Submit decodes the BEEF once into the step’s write cache, runs SPV, and asks topic managers <code>identify(tx: cid, …)</code>. <b>Nothing persists unless a topic admits</b>, apart from the request itself; otherwise it answers 200 with an empty STEAK. A transaction is admitted on the first of an accepted status or a validated proof. Lookup services keep their own maps and get <code>admitted</code>/<code>spent</code>/<code>rejected</code> hooks. The stock <code>@bsv/sdk</code> broadcaster and resolver work against an overlay at an origin’s root (tested); they reject a base URL with a path, so skein does not use them for installed overlay apps."
   - Change "the store is byte-identical": since #68 the request is an entry, so the store is no longer byte-identical. Drop it.
6. **L311**, **built** + **decided-not-built (#79)**
   - now: "Not built: SHIP/SLAP advertisement, GASP sync, certificates, header catch-up, proofs on demand. One broadcaster per host is designed."
   - proposed: "Not built: SHIP/SLAP advertisement, GASP sync, certificates, header catch-up, proofs on demand. Being built (#79): each overlay’s state under its own name, so two overlays can run on one instance."

### (c) Badges
- The page has none. Optionally add `designed` next to the #78/#79 sentences.

### (d) New
- Covered: the chain app (#78) and the re-split (#79).

---

## 17. Genesis and deployment (l3-tech.html, L324–363) — add a section

### (a) Still right, stays
- Lede (L327). "Two sources, one loader" (L340–343). Checkpoints (L346). The not-built list (L353) stays true.

### (b) Changes
1. **L331–336** (system tree block), **built** — BOOTSTRAP.md "The system tree"
   - now: the block lists `etc/config.json defaults, peers, feeds, owner, libp2p`, `etc/subscriptions.json (sender, box) → program (required)`, `etc/routes.json HTTP path → program fn`, `etc/reads.json`.
   - proposed:
     ```
     bin/<name>.wasm | .cid | .json   programs
     etc/config.json                   defaults, names, feeds, owner, libp2p, scopes
     etc/dispatch.json                 rows: box | HTTP path | libp2p topic → program
     etc/reads.json                    who may call read routes
     SOUL.md, IDENTITY.md, skills/…    the instance's own files
     ```
     (subscriptions.json and routes.json are still read and converted; don't list them.)
2. **L337**, **built** — BOOTSTRAP.md; VM.md "The genesis carries the seed"
   - now: "Booting pre-fills the store and writes a genesis naming the tree; processing it sets head <code>main</code>. The genesis also fixes the owner, the default limits and the owner’s mailbox for the life of the store."
   - proposed: "Booting pre-fills the store and writes a genesis naming the tree; processing it sets head <code>main</code> and seeds the dispatch table: the owner’s four admin rows first, then the tree’s. The genesis also fixes the owner, the default limits, the owner’s mailbox and the host’s providers in the address book."
3. **L348–349** (Deploying files vs booting), **built** — VM.md "The admin operations"
   - now: "…go in through the <code>objects</code> box as an ordinary signed message from the owner."
   - proposed: "…go in as an ordinary signed message from the owner to the kernel’s <code>objects</code> operation."
4. **L351–352** (Upgrades are re-genesis), **built**; h2 → "Upgrades" — APPS.md §3 "Reconfiguration"; kernel-zig/README.md "Format 8"
   - now: "New program versions apply to new geneses; an existing store keeps the modules its genesis names, and older formats aren’t migrated. Upgrading today means a new store."
   - proposed: "An app upgrades by being installed again. Its state is kept, and rows the new version no longer asks for are removed. A change to the kernel’s log format (format 8 today) still means a new store: older formats are refused, not migrated."
5. **L360** (card) stays.

### (c) Badges
- None today; add `built` / `not decided` in the new section (d).

### (d) New
- New h2 after "Deploying files vs booting": **"Installing an app"**, **built** (APPS.md §2–3; BOOTSTRAP.md "Installing an app"; #72, #76, #77):
  "An app is a tree with <code>etc/app.json</code>: its programs, its configuration, what it provides and requires, the dispatch rows it asks for, and optional start and stop messages. <code>skein-host install &lt;repo | dir&gt; --instance &lt;handle&gt;</code> checks it and reads the rows aloud. Once the owner approves, it sends four kinds of admin message: <code>objects</code> (the tree and program records), <code>head</code> (<code>&lt;app&gt;/app</code> → the app record), <code>dispatch</code> (one per row; web paths under <code>/&lt;app&gt;/</code>), then <code>start</code>. An app writes only heads under its name. Uninstall sends <code>stop</code> and removes its rows. `built`"
  Then: "Every genesis carries the owner’s admin rows. A bare genesis with a bundle of apps installed on top is the direction; the bundle’s format is not decided. `not decided`"
- Optional: rename the page h1/TREE title to "Genesis, apps and deployment" (shell.html L238 and l3 L326). Same page, no new page.

---

## 18. What is built (l3-tech.html, L366–385) — rewrite every row

### (b) Changes (all from #77 close comment, #31 State, APPS.md §7)
1. **L369** lede: "Status by area, as of the end of September 2026." → "Status by area, as of 1 October 2026 (log format 8)."
2. **L373** Kernel, **built**: add "four tables (objects, heads with owners, dispatch, address book), admin operations in the kernel, write scope by app name."
3. **L374** Userland: unchanged.
4. **L375** Network, **built**; drop the `designed` part
   - proposed: "`built` Front door stepped on every request, sessions as records, the dispatch table, mailbox instances, messagebox, address book, discovery, <code>emit</code> and providers (fetch, waker, cron, libp2p, status), delivery threads, libp2p on every transport, overlay gossip."
5. **L376** Wallet, **built** + **decided-not-built**
   - proposed: "`built` Oracle interface, wallet program, SPV, sparse proofs, settlement, broadcast as an event, status provider. `designed` The chain app (#78); the wallet under its own name (#79). `not yet` Header catch-up, proofs on demand, certificates."
6. **L377** Overlay
   - proposed: "`built` Overlays as apps, topic managers and lookup services on CIDs, libp2p gossip, one broadcaster per host. `designed` Each overlay’s state under its own name, two overlays per instance (#79). `not yet` SHIP/SLAP, GASP."
7. **New row "Apps"** (after Overlay), **built**
   - "`built` Manifest, install/uninstall with approval, app record under <code>&lt;app&gt;/app</code>, start/stop, the SDK’s <code>app.serve</code>; apps in their own repos (workbench, static, overlay). `designed` Stock manifests in the new shape (#79). `not decided` Bundles."
8. **L378** Inference: unchanged.
9. **L379** Deployment: append "`built` App upgrade by reinstall."; keep "`not yet` Publishing on chain, commit-ID boot."
10. **L380** Hosting & payments, badge change
   - now: "`built` Metering. `designed` Payment channel billing, stand-up flow, tolls on messages. `not yet` Public hosting, prices."
   - proposed: "`built` Metering. `not decided` Billing, how to get a skein from a host, payments between skeins. `not yet` Public hosting, prices."
11. **L381** Graph ops: unchanged.
12. **L383** suites, **built** — #77 close comment
   - now: "Latest suites: kernel 45/45, wallet 25/25, overlay 2/2, npm 124/124, equivalence 199 ok, 0 fail."
   - proposed: "Latest suites (main 063d30b): kernel 35/35, npm 154/154, equivalence all ok (18/18 histories identical, browser replays included)."
   - The wallet and overlay suites now live in skein-sdk and skein-overlay. Either drop them or cite those repos’ own counts once checked.

---

## Pages whose structure should change

- **t-arch** (L69–76) "The kernel’s whole surface": rows become admit · answer · call · wallet · emit. `http` and `libp2p` go and `answer` and `emit` come in. The diagram (L9–54) needs a redraw: host boxes become transports / oracle / providers / broadcaster + feeds / store / fuel ledger with no routing box, plus a four-tables strip in the kernel and the programs split into boundary programs and apps. "Runtimes" becomes "Hosts".
- **t-vm** (L200–204) syscall table: "Recorded" shrinks to the oracle. "Graph" splits into Reads / Writes / Threads (the #31 kernel-call inventory), and a new "Out: emit" row is added.
- **t-net**: the persistence table (L251–257) keeps its five rows with new content (every row is now "its request entry, and…"). "Routing inside" becomes "The dispatch table". Add one section, "One way out: emit and the providers". Five sections become six.
- **t-deploy**: add "Installing an app" and turn "Upgrades are re-genesis" into "Upgrades". Optionally rename the page "Genesis, apps and deployment".
- **t-status**: add an "Apps" row.
- **keys** (l2): "Only state gets written" flips to "Everything that arrives is written". The door table gets one row.
- **running** (l2): "How it would pay" and "Getting one" each shrink to a short `not decided` paragraph. The page keeps its three headings.
- No new pages. Apps are a new concept, but they fit t-arch (what they are), t-deploy (installing) and t-wallet (the overlay as an app). If David wants a page, a "t-apps" between t-wallet and t-deploy would be the one candidate.

## Not to put on the site (undecided or parked)
- The storage scope map / kernel-vs-user store hierarchy (#31 "Discussed… not yet decided").
- Bundle format (say only "not decided").
- Parallel steps (parked).
- Billing, payment channel, stand-up flow, locator token, skein.nexus as a management UI (#39, #11).
- Origin-per-app routing (parked).
- The eleven #77 "David to review" calls (row key shape, transitional grants, legacy manifest conversion, `local` rows not firing, the resolve program writing `peers`). These are internal and nothing on the site depends on them. The only site-visible one: http rows are confined to `/<app>/`, which the plan states as built.

## Build / deploy state
- `index.html` and `dist/index.html` match a fresh assembly of shell.html + the four parts (checked by re-running build.py’s assembly in memory; no files written).
- The live https://skein.nexus/ is byte-identical to `dist/index.html` (fetched tonight). So the site is live and unchanged since 2026-09-29 22:41.
- `wrangler.jsonc`: name `skein-nexus`, assets `./dist`, custom domain `skein.nexus`, compatibility date 2026-09-26. `.wrangler/cache` holds an account id from the 09-29 deploy. Deploy = `python3 build.py` then `wrangler deploy` from site-v2 (needs that Cloudflare login).
- skein-nexus/ is **not a git repository**: no history of the site, and nothing to diff against. Worth `git init` before the rewrite.
- `og.png` is built only when `chromium` is on PATH; the og/meta copy (shell.html L2–11) is still accurate.
- Tree titles in shell.html (L222–241) change only if t-deploy is renamed.

## Summary

About a quarter of the site is affected in substance, and nearly all of it sits in the technical pages and two l2 pages. **Mostly fine, light edits:** the Overview (two sentences and the legend), the Sandbox page (one table row and tone), the Graph page (one line plus two short additions), Traceable inference (no change), One graph of your work (no change), Start from a commit (one sentence plus an apps paragraph), and Data model (word-level). **Moderate:** Keys and the door (the persistence section flips, one door row is rewritten and goes from designed to built, signer → oracle), A skein per agent and Skeins together (dev-only framing, payments marked not decided, the overlay paragraph rewritten as an app), Your slice of Bitcoin (feeds sentence, chain app as designed), The kernel and VM (the syscall table and the time paragraph), and What is built (every row redated, an Apps row, hosting moved to not decided). **Rewrites:** Architecture (lede, diagram, surface table, programs/apps, hosts), Messages and network (lede, front door, routes, persistence table, dispatch table, delivery, libp2p, plus a new emit/providers section), Wallet and overlays (oracle, feeds → broadcasts/proofs/statuses, overlays as apps, the #78/#79 split), Genesis and deployment (system tree, an Installing-an-app section, upgrades), and Hosting, cost, and getting one (host jobs restated; billing and stand-up cut to "not decided"). The three-level structure holds; no new page is needed.

---

# Walkthrough with David, 2026-10-01 night — rulings so far (override the plan above where they differ)

**Global rules**
- The site documents what is *settled*, in the present tense. Drop the built / in progress / designed badges everywhere. One status table stays (page 18) for build status. Say "not decided" only where a topic must be mentioned.
- Vocabulary for the audience: "signer", not "oracle". No "stock" anything. No "workbench": the shell app and the chat app (#83). A userland is the shell app, not a default. "host" for the thing that runs a skein.
- Payments are a capability (BRC-169 carries a transaction; BRC-29 in the wallet); do not back away from them; do not mention negotiation status.
- Remove the "Running today" box (page 6); what is running is out of place on the site.
- Cross-cutting pass to do: audit every use of "agent", "autonomous", "AI" across the four parts; the site means both the old sense (an autonomous workflow engine) and the new one (a model driving); state the distinction once, early, and use the right word in each place.
- Open: the hero "A computer with its own keys and a complete memory" is weak — "its own keys" speaks to a narrow audience; find a wider thesis (not solved yet).

**Page 1 Overview**: keys pillar edit as planned; keep "message and pay each other" (payments are a capability); legend wording: status lives only on the status page; add the apps sentence as planned.
**Page 2 Sandbox**: L11 → "A userland is itself an app, the shell. A skein that installs it can run:"; network row as planned; L37 → "A step's inputs are all in the history: the entry that woke it, what it read, and what it had signed." (the signer is infrastructure like storage — don't single it out); tone edits as planned.
**Page 3 Keys and the door**: keep "signer" (no oracle rename). Wallet paragraph: "Its coins and transactions are records in the graph like everything else. It builds and signs transactions (through the signer) and checks incoming payments against their proofs before it accepts them. Block headers, proofs and transaction status live in one chain app that the wallet and every overlay read." Replace L76 with a host lead-in + the door paragraph: "A skein runs on a host. The host runs the kernel, holds the keys, and provides, or points to, the transports and services the skein's tables name: a web proxy, a mailbox, libp2p, a broadcaster, timers. A skein moved to another host that provides the same things runs the same, with the same history." then "A skein has no server of its own. The host carries packages in over whatever transports the skein's dispatch table names: HTTP, a mailbox, libp2p. Each package is written to the history as it arrived, and the program the table names for it runs on it. For HTTP that program is the front door, which checks mutual authentication (BRC-103/104) before anything else sees the request." Door row "Something the skein asked for": "The skein asks a service, a web proxy or a timer, and waits. The service may be its host's or anyone's, since it is only an address in the skein's book. The reply is written into the history, signed by whoever answered." Section heading/text "Everything that arrives is written" as planned. New door row: "A transaction's status: Arcade, the service the skein broadcast to, reports back as the transaction is accepted and mined." Captions as planned.
**Page 4 Graph**: L125 → "Steps programs took, with the work they cost, what they read, and what they had signed."; tables addition as planned; heads addition: "Every head belongs to one app, and its name says which: `wallet/…` is the wallet's. An app can move only its own heads. Any program can read any record whose hash it holds."
**Page 5 Model**: add "The conversation loop is an app of its own, the chat app; a shell is another."
**Page 6 Agents**: dispatch sentence as planned; remove the "Running today" box; keep "signer".
**Page 7 Together**: L129 → "A rejected one is refused and kept in the history; a repeat is ignored." Overlay paragraph: "An overlay is an app: the overlay engine plus your own topic managers and lookup services, installed under one name. It takes transactions for its topics at `/<handle>/<app>/submit`, keeps the ones its rules admit, answers lookups, and shares what it admitted with peers over libp2p. If no topic admits a transaction, only the request is recorded. BSV-21 tokens and 1Sat Ordinals collections are the first overlays being written for it." (no AMM). Paying: "A skein's wallet can receive a payment and make one, and a payment can ride on any message: to pay for work, or to pay for delivery to a mailbox." Note: "Why the record matters here. Programs that message each other and hold money should be inspectable. Every message between them is signed, every step is kept, nothing can be deleted or rewritten, and any step can be re-run." Card caption as planned.

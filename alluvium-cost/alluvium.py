#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ALLUVIUM
========
A register of the riverbed, laid down by many small waters.

        Upon those who step into the same rivers
        other and other waters flow.
                                        -- Heraclitus, as the fragment is kept

This is one file, and it is the whole of the work: the vision, the ordinances
by which it is carried out, and the labor itself. Read it through once before
running it. What follows is not a preface to the code; the code is the same
telling continued in another hand.


I. OF THE TWO WAYS OF KNOWING A THING
-------------------------------------

The potter knows the vessel by what it is made of. He begins with clay and
water; he adds, he turns, he fires; and when he is asked what the vessel is,
he recites its making. The old philosophers called this substance: that which
stands under, that from which the thing is built. The logicians of our own
day call it algebra. A thing is a term, assembled from its constructors, and
to reason about it you take it apart the way it was put together. Induction
is the potter's way. The whole is known from the parts.

The ferryman knows the river by how it carries him. He has never seen all of
it and never will, for by the time he looks it is other water. He is asked
whether this is the same river as yesterday's, and he does not answer with
substance. He answers: it takes my boat the same way at the ford, it rises
the same at the narrows, it is quiet the same beneath the willows. The
logicians call this coalgebra. A thing is a state, known only by its
unfolding under observation, and to reason about it you do not take it apart;
you watch what it does. Coinduction is the ferryman's way. The thing is known
from its flowing, and two flowings that no crossing can tell apart are, for
every purpose a crossing can serve, one.

Heraclitus, who said that other waters flow upon those who step into the same
river, was not denying that the river has a name. He was saying how the name
is earned.


II. OF SAMENESS AND FORGERY
---------------------------

Ask whether the one standing at the gate is Alice.

The potter's answer compares what she is made of against what was recorded of
her: the line of a face, the pressure of a hand, the hours she keeps. This is
how the age verifies. But a recording of substance is a cistern. It goes
stale; it cannot forget; and it is where thieves go, for what is stored can be
stolen, and what is stolen of a face cannot be changed as a key can.

The ferryman's answer is older and stranger. She is Alice if she carries you
the way Alice carries you, under every crossing you are permitted to attempt.
Sameness is a relation on flowings. Two states are bisimilar when each move of
the one is matched by a move of the other, and the states so reached are
bisimilar again, down and down without end. A forgery, then, is not a thing of
false substance. It is a flow that would behave otherwise under some crossing.
To detect it is to find the crossing. And if no permitted crossing finds it,
then by the only sameness that matters it is not a forgery at all, which is a
hard saying, and true.

Hence the asset. Not the recording of Alice, but the set of crossings
permitted: which questions may be asked, which measures taken, which witnesses
heard. Fix too few and every stream is the same stream, and the forger walks
through. Fix too many and the honest ferry fails against the current, for
people change -- they age, they fall ill, they move among strangers -- and a
sameness that admits no drift admits no one. The elders Hennessy and Milner
showed that the crossings may be written as a small grammar of tests (there is
a move labeled so, after which such-and-such; not; and both), and that two
flows which no test of that grammar tells apart are bisimilar. The tests are
terms, built up by the potter. The flows are states, known by the ferryman.
Both are right, each about its own side of the water.

We give the set of crossings a name. In the tongue of those who write
coalgebras it is the Signature, the signature of the functor, fixed before any
state exists and defining what a state can be asked. Because all else in this
register flows from it, we also call it the Spring.


III. OF WHERE THE REFERENCE IS KEPT
-----------------------------------

Yet the ferryman's way needs a reference too. To say Alice behaves as Alice
did, something must remember how Alice did. Record her whole flowing and you
have built a cistern worse than the first: continuous, contextual, telling not
only her face but her intent and her company.

The oldest answer is the village. Bob knows Alice. Not entirely -- he forgets,
he is sometimes wrong, he can be threatened or bought -- but he can be asked,
he can be held to his word, and when he is gone his knowledge goes with him,
which no ledger does. The trusted neighbor is a lossy, accountable,
adversarially robust compression of an equivalence class; which is a grand way
of saying that the village has always done this, by witnesses and seals. The
clay tablets of Mesopotamia list, after the terms of a sale, the names of
those who saw it. By the mouths of two or three witnesses a matter is
established. One neighbor may be bought; a quorum is dearer; a quorum drawn by
lot, with stake to lose, with its chains of vouching fading like a voice
called across water, is dearer still. Set the first witnesses on institutions
that can be sued, route the small daily matters through cryptography and keep
the neighbors for the grave and the ambiguous, and you have the whole
architecture. It is not new. What is new is only to write it in the
ferryman's language, and to see that its failures -- coercion, bias, cabal,
the regress of who vouches for the vouchers, the weariness of those asked too
often -- are not failures of detection. They are matters of rule: bisimilar
under which crossings, against which adversary, with what room for error, for
how long, and who commands the witnesses.


IV. OF THE MANY SMALL WATERS
----------------------------

We have at hand a great number of laborers, cheap as rain, each a little
stream of intelligence. No single one is to be trusted; a drop is not trusted.
But rain gathers to rills, rills to brooks, brooks to tributaries, and the
river is trusted though no drop is. What the river leaves behind, season upon
season, is not water but bed: the silt that settles, the alluvium on which
later water finds its way and later people build. This file directs the rain
so that it lays down bed.

What it lays down is not a record of persons. That is the Interdict, and it
is the first ordinance: we chart the riverbed, not the swimmers. The register
holds crossings and the winds that break them, villages and the customs by
which they vouch, floods remembered, boundary stones, the mill's tables, and
the sayings of the elders. It holds no one's face.


V. THE SIX TRIBUTARIES
----------------------

The Crossings.      Every known test by which one flow is told from another:
                    what it distinguishes, what it costs, how often the forger
                    passes and the honest fails, what it reveals, whether it
                    serves when the directory is unreachable; and, paired to
                    each, the winds that break it.

The Villages.       Where people already vouch for one another: savings
                    circles, remittance corridors, responder companies,
                    maintainer webs, the block committees of camps, the
                    guardians of the failing; how thick the acquaintance is,
                    by what custom they vouch, under what penalty, how they
                    settle disputes, on what institution they are anchored;
                    and the bridges by which one village's word may be carried
                    to another.

The Floods          When vouching has failed in the open record -- the false
  Remembered.       notarization, the bribed clerk, the ring of mutual
                    vouchers, the guardian who emptied the estate -- and of
                    which kind each failure was.

The Boundary        Under which laws a witness may be held to a word, who
  Stones.           must repay a fraud, how a mind in decline is supported
                    rather than silenced, what identity a disaster permits.

The Mill.           What the wheel computes when turned: for quorum, cartel,
                    decay, and the thickness of acquaintance, where forgery
                    grows cheap and where the honest are shut out; and the toy
                    ford at which the lesson of the Signature is shown in
                    small.

The Elders.         What those before us wrote of sameness, of witness, of
                    Sybils, of trust that fades with distance, that bears on
                    the bed we are laying.


VI. THE LABORERS
----------------

The Dowser.      Vitruvius taught that one finds a spring by lying face down
                 on the ground before dawn and watching where the mist curls
                 up. The dowser goes out with a tributary's question and
                 returns with places where water may be, each marked with
                 where it was found. The dowser fills nothing.

The Scribe.      Draws from the place the dowser marked and fills the
                 destructors of its kind: what the thing does under each
                 observation the Signature permits. Where the source is
                 silent the scribe writes "unknown," which is a kind of
                 honesty the cistern never learned.

The Winnower.    On the threshing floor the grain is thrown into the air and
                 the wind takes what is light. Every crossing the register
                 believes in is thrown to the wind of an adversary: the
                 winnower's charge is to find the attack under which an honest
                 flow and a forged one become bisimilar, so that the crossing
                 no longer crosses. What the wind takes was chaff.

The Assayer.     Frontinus, curator of the waters of Rome, found the pipes
                 tapped in secret and the register's figures false, and he
                 measured again. The assayer is given a proposal another
                 laborer made and must not be gentle with it: does the source
                 as drawn support what is written; does the thing keep the
                 Interdict; is it specific enough to be wrong. The assayer did
                 not make the proposal, and no two assayers of one proposal
                 are the same laborer.

The Millwright.  Turns the wheel. Whatever can be computed is computed, and
                 its witness is the wheel itself: turn it again and it will
                 say the same. That is the only witness the mill is permitted.

The Surveyor.    At the end of each day walks the bed and marks where it is
                 thin, which crossings stand unwinnowed, which proposals wait
                 for seals; and from that map sets the morrow's labor.


VII. THE ORDINANCES
-------------------

1. No spring, no stream.      A proposal without a source is a mirage. It is
                              written down as a mirage, so that the dowser
                              who saw it is remembered, and it is never bed.

2. Every grain to the wind.   No crossing is settled and left in peace. Each
                              one settled summons a winnower.

3. By several mouths.         A proposal is bed when k of n assayers, none of
                              them its maker, none of them each other, have
                              sealed it sound. Where more than one voice is
                              available, each laborer drinks always from the
                              same hill, so that the assayers of a proposal
                              may come from other hills than its proposer,
                              and their agreement means more.

4. The moon seals the bed.    At the turning of the month, or when commanded,
                              the settled bed is copied whole into the almanac
                              with the date upon it, and what is copied is
                              never altered. Later work cites a dated bed.

5. The surveyor rules the     Nothing is scheduled from fancy. The map of
   morrow.                    what is thin is the only schedule.

6. The Interdict.             We chart the riverbed, not the swimmers. No line
                              of code keeps this ordinance. The assayers keep
                              it, and the keeper of this file keeps it; and
                              that is the whole telling in small: the last
                              guard of any register is a person who can be
                              held to a word.

Beneath these, one more that is not an ordinance but a warning. The rain is
cheap, and cheap voices confabulate: they will name a source that does not
exist as readily as one that does. The ordinances above are the levee against
this. They do not make a drop trustworthy. They make the river so.


VIII. OF THE ORACLE, AND HOW THE WORK IS BEGUN
----------------------------------------------

The laborers speak through whatever cheap voice answers in the common dialect
of the age: any service that accepts a "chat completions" request at a base
address, which nearly all of them do, including those that run on one's own
hearth. Set three things in the air before you call:

    ALLUVIUM_API_BASE   the address, up to and including the "/v1"
    ALLUVIUM_API_KEY    the token, if the gate asks one
    ALLUVIUM_MODELS     one model name, or several set with commas; use the
                        cheapest capable voices you have, and more than one
                        if you can, for the reason given in ordinance 3

Then:

    python alluvium.py --cycles 12 --workers 16      twelve tides of labor
    python alluvium.py --dry --cycles 4              a rehearsal: no voice,
                                                     sand laid, not silt
    python alluvium.py --freeze                      seal the bed now

The register lives in ./alluvium (or ./alluvium-rehearsal for a dry run).
strata.jsonl is the sediment, append-only, every event a stratum; almanac/
holds the sealed beds. Run it in the background, a few tides each day, for as
long as you have rain. It stops where you stop it and begins again where it
left off, for the bed remembers.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from typing import Any, Callable, Optional


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def say(text: str) -> None:
    """The day-book. Everything the laborers do is spoken once, aloud."""
    sys.stderr.write(f"[{datetime.now().strftime('%H:%M:%S')}] {text}\n")


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def digest(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()[:16]


# =============================================================================
# I. THE SPRING
#
# The Signature is fixed here, before any state exists. For each kind of state
# it names the destructors: the observations a state of that kind must answer
# to. Nothing is added to the Signature by the laborers. Only the keeper of
# this file may widen the Spring, and should do so rarely, for every state
# already laid was laid under the old one.
# =============================================================================

INTERDICT = (
    "We chart the riverbed, not the swimmers. No state in this register may "
    "be, or may serve to identify, a private living person. The register holds "
    "mechanisms, institutions, customs, incidents already in the public record, "
    "laws, computations, and the sayings of the elders. It holds no one's face, "
    "no one's gait, no one's hours, no one's company."
)

SIGNATURE: dict[str, tuple[str, ...]] = {
    "observation":      ("distinguishes", "cost", "false_accept", "false_reject",
                         "privacy_cost", "works_offline", "broken_by"),
    "adversary":        ("capabilities", "cost_to_mount", "defeats"),
    "attack":           ("against", "makes_indistinguishable", "mounted_by", "countered_by"),
    "mechanism":        ("function", "bounds", "fails_when"),
    "cluster":          ("population", "density", "vouching_custom", "sanction",
                         "dispute_custom", "anchoring"),
    "bridge":           ("from_cluster", "to_cluster", "signature_overlap",
                         "stake_bound", "decay_bound"),
    "incident":         ("what_happened", "failure_mode", "mechanism_implicated", "year", "lesson"),
    "failure_mode":     ("surface", "mitigation", "residual"),
    "jurisdiction":     ("attester_liability", "reimbursement_regime",
                         "supported_decision_law", "identity_law", "emergency_provision"),
    "use_case":         ("stakes", "volume", "binding_condition", "verdict"),
    "parameter_result": ("parameters", "forgery_probability", "exclusion_rate", "finding", "method"),
    "claim":            ("asserts", "work", "author", "year", "bears_on"),
}

# What each destructor asks. The scribe is given these glosses, so that the
# question put to the source is the same question every time.
GLOSS: dict[str, str] = {
    "distinguishes":           "which flows this crossing tells apart",
    "cost":                    "what it costs to apply, in money, time, and friction for the honest",
    "false_accept":            "how often the forger passes, as reported",
    "false_reject":            "how often the honest fail, as reported",
    "privacy_cost":            "what it reveals, and what must be stored to apply it",
    "works_offline":           "whether it serves when the central directory is unreachable",
    "broken_by":               "the known winds that make two flows one under it",
    "capabilities":            "what this adversary can do and observe",
    "cost_to_mount":           "what it costs the adversary to act",
    "defeats":                 "which crossings this adversary is known to defeat",
    "against":                 "the crossing this attack is thrown at",
    "makes_indistinguishable": "which honest flow and which forged flow become bisimilar under it",
    "mounted_by":              "which adversary can mount it, and at what cost",
    "countered_by":            "what further crossing would tell the flows apart again",
    "function":                "what the mechanism does in the architecture",
    "bounds":                  "what it bounds, and by how much",
    "fails_when":              "under what conditions it stops bounding",
    "population":              "how many, roughly, and who",
    "density":                 "how many members a typical member is known to, roughly",
    "vouching_custom":         "by what custom members already vouch for one another",
    "sanction":                "what befalls a member who vouches falsely",
    "dispute_custom":          "how disputes are settled, and by whom",
    "anchoring":               "on what institution, if any, the cluster rests",
    "from_cluster":            "the cluster whose word is carried",
    "to_cluster":              "the cluster that receives it",
    "signature_overlap":       "which crossings both clusters already honor",
    "stake_bound":             "what stake makes the carried word costly to forge",
    "decay_bound":             "how the carried word fades with distance",
    "what_happened":           "the course of the failure, briefly",
    "failure_mode":            "which of the register's failure modes it was",
    "mechanism_implicated":    "which mechanism failed or was absent",
    "year":                    "when",
    "lesson":                  "what it teaches about the bed we are laying",
    "surface":                 "where the failure enters",
    "mitigation":              "what is known to narrow it",
    "residual":                "what remains after mitigation",
    "attester_liability":      "whether and how a witness or notary may be held liable",
    "reimbursement_regime":    "who must repay a fraud, and under what rule",
    "supported_decision_law":  "how the law supports, rather than replaces, a failing mind",
    "identity_law":            "what the law counts as legal identity, and how it is enrolled",
    "emergency_provision":     "what identity a disaster or displacement permits",
    "stakes":                  "what is lost if verification is wrong",
    "volume":                  "how often it occurs",
    "binding_condition":       "which condition binds: breach asset, inclusion, availability, dismantling, or none",
    "verdict":                 "whether the village or the cistern or the key serves here, and why",
    "parameters":              "the settings given to the wheel",
    "forgery_probability":     "the chance a cartel passes",
    "exclusion_rate":          "the chance an honest person cannot find a quorum",
    "finding":                 "the lesson in a sentence",
    "method":                  "how the wheel computed it",
    "asserts":                 "the claim in one sentence",
    "work":                    "the title of the work",
    "author":                  "who wrote it",
    "bears_on":                "which part of the bed it bears on",
}


@dataclass(frozen=True)
class Tributary:
    name: str
    kinds: tuple[str, ...]
    question: str
    floor: int  # settled states below which the surveyor calls it thin


TRIBUTARIES: tuple[Tributary, ...] = (
    Tributary("the crossings", ("observation", "adversary", "attack"),
              "Which crossings tell one flow from another, and what wind makes two flows one again?", 12),
    Tributary("the villages", ("cluster", "bridge", "mechanism"),
              "Where do people already vouch for one another, by what custom, under what penalty, "
              "and how may one village's word be carried to another?", 10),
    Tributary("the floods remembered", ("incident", "failure_mode"),
              "When has vouching failed in the open record, and of which kind was the failure?", 10),
    Tributary("the boundary stones", ("jurisdiction", "use_case"),
              "Under which laws may a witness be held to a word, who must repay a fraud, "
              "and how is a mind in decline supported rather than silenced?", 8),
    Tributary("the mill", ("parameter_result",),
              "For quorum, cartel, decay, and the thickness of acquaintance, "
              "where does forgery grow cheap and where do the honest fail?", 24),
    Tributary("the elders", ("claim",),
              "What have those before us written of sameness, of witness, of Sybils and of trust "
              "that fades with distance, that bears on the bed we are laying?", 12),
)
TRIBUTARY_BY_NAME = {t.name: t for t in TRIBUTARIES}


# =============================================================================
# II. STATES AND WITNESSES
#
# A State is the ferryman's object: a kind, a name, and an unfolding, which is
# what it does under each destructor of its kind. A Witness is the potter's
# object: a finite term with a source, a drawn excerpt, a laborer, a date. The
# first is known by flowing; the second is built, and can therefore be
# audited. A Proposal binds the two and waits for seals.
# =============================================================================

def _key(kind: str, name: str) -> str:
    return hashlib.sha256(f"{kind}|{name.strip().lower()}".encode()).hexdigest()[:16]


@dataclass
class State:
    kind: str
    name: str
    unfolding: dict[str, Any] = field(default_factory=dict)

    @property
    def key(self) -> str:
        return _key(self.kind, self.name)

    def conforms(self) -> bool:
        """A state conforms when its kind is in the Signature and it answers
        only to destructors the Signature permits for that kind."""
        if self.kind not in SIGNATURE:
            return False
        return all(d in SIGNATURE[self.kind] for d in self.unfolding)


def filled(state: State) -> int:
    """How many destructors the state answers with something other than silence."""
    return sum(1 for v in state.unfolding.values()
               if v not in (None, "", "unknown", [], {}))


@dataclass
class Witness:
    source: str          # where the water was found: a locator, a citation, "conjecture: ...", "mill://..."
    drawn: str           # what was drawn from it: an excerpt or faithful summary
    agent: str           # the laborer who wrote it down
    when: str
    confidence: float = 0.5
    found_by: str = ""   # the dowser, where there was one

    def is_sourced(self) -> bool:
        s = (self.source or "").strip().lower()
        return bool(s) and s not in ("none", "unknown", "n/a", "")


@dataclass
class Seal:
    assayer: str
    verdict: bool
    reason: str
    when: str


@dataclass
class Proposal:
    state: State
    witness: Witness
    seals: list[Seal] = field(default_factory=list)
    status: str = "suspended"    # suspended | settled | washed | mirage
    rehearsal: bool = False
    stratum: int = 0

    @property
    def key(self) -> str:
        return self.state.key

    @property
    def sid(self) -> str:
        return f"{self.key}#{self.stratum}"

    @property
    def ayes(self) -> int:
        return sum(1 for s in self.seals if s.verdict)

    @property
    def nays(self) -> int:
        return sum(1 for s in self.seals if not s.verdict)


def proposal_from_dict(d: dict[str, Any]) -> Proposal:
    return Proposal(
        state=State(**d["state"]),
        witness=Witness(**d["witness"]),
        seals=[Seal(**s) for s in d.get("seals", [])],
        status=d.get("status", "suspended"),
        rehearsal=d.get("rehearsal", False),
        stratum=d.get("stratum", 0),
    )


def render(p: Proposal) -> dict[str, Any]:
    """The proposal as it is shown to an assayer: state and witness, no seals."""
    return {
        "kind": p.state.kind,
        "name": p.state.name,
        "unfolding": p.state.unfolding,
        "witness": {"source": p.witness.source, "drawn": p.witness.drawn,
                    "confidence": p.witness.confidence},
    }


# =============================================================================
# III. THE TERM ALGEBRA OF TESTS
#
# Here the potter's side and the ferryman's side touch. A Formula is a term:
# built up from constructors, finite, something you can write on a tablet. A
# transition system is a coalgebra: states known by what moves they afford.
# A formula that one state satisfies and another does not is a crossing that
# tells them apart. If no formula of bounded depth tells them apart, and the
# partition refinement below says they lie in one block, they are bisimilar
# under that set of crossings, and the forger walks through.
# =============================================================================

LTS = dict[str, dict[str, set[str]]]   # state -> action -> states reached


class Formula:
    pass


@dataclass(frozen=True)
class Top(Formula):
    def __str__(self) -> str:
        return "T"


@dataclass(frozen=True)
class Dia(Formula):
    """<a>phi: there is a move labeled a, after which phi."""
    action: str
    body: Formula

    def __str__(self) -> str:
        return f"<{self.action}>{self.body}"


@dataclass(frozen=True)
class Neg(Formula):
    body: Formula

    def __str__(self) -> str:
        return f"not({self.body})"


def holds(phi: Formula, s: str, lts: LTS) -> bool:
    if isinstance(phi, Top):
        return True
    if isinstance(phi, Neg):
        return not holds(phi.body, s, lts)
    if isinstance(phi, Dia):
        return any(holds(phi.body, t, lts) for t in lts[s].get(phi.action, ()))
    raise TypeError(phi)


def bisimilar(lts: LTS, p: str, q: str, crossings: tuple[str, ...]) -> bool:
    """Partition refinement. Begin with every state in one block; split each
    block by what moves its states afford into which blocks; repeat until the
    water is still. Two states in one block at the end are bisimilar under
    these crossings, and under these only."""
    states = list(lts)
    block = {s: 0 for s in states}
    while True:
        signature = {
            s: (block[s], frozenset((a, block[t]) for a in crossings for t in lts[s].get(a, ())))
            for s in states
        }
        ids: dict[Any, int] = {}
        refined = {s: ids.setdefault(signature[s], len(ids)) for s in states}
        if len(set(refined.values())) == len(set(block.values())):
            return refined[p] == refined[q]
        block = refined


def distinguishing(lts: LTS, p: str, q: str, crossings: tuple[str, ...], depth: int = 3) -> Optional[Formula]:
    """Search the small grammar for a test that p passes and q fails, or the
    reverse. Conjunction is omitted; the toy ford below needs none."""
    level: list[Formula] = [Top()]
    for _ in range(depth):
        nxt: list[Formula] = []
        for phi in level:
            for a in crossings:
                nxt.append(Dia(a, phi))
            if not isinstance(phi, Neg):
                nxt.append(Neg(phi))
        for phi in nxt:
            if holds(phi, p, lts) != holds(phi, q, lts):
                return phi
        level = nxt
    return None


# The ford. Three flows present themselves at the gate. One is Alice. One is a
# mask that has learned the credential and the challenge. One is Alice with a
# knife at her back. The sensor can catch the mask, if it is permitted the
# crossing of shared memory. Only a neighbor catches the knife.
CROSSINGS: tuple[str, ...] = ("present", "answer_challenge", "recall_shared_past", "show_duress")
FORD: LTS = {
    "alice":     {"present": {"alice/1"}},
    "alice/1":   {"answer_challenge": {"alice/2"}, "recall_shared_past": {"alice/3"}},
    "alice/2":   {}, "alice/3": {},
    "mask":      {"present": {"mask/1"}},
    "mask/1":    {"answer_challenge": {"mask/2"}},
    "mask/2":    {},
    "coerced":   {"present": {"coerced/1"}},
    "coerced/1": {"answer_challenge": {"coerced/2"}, "recall_shared_past": {"coerced/3"},
                  "show_duress": {"coerced/4"}},
    "coerced/2": {}, "coerced/3": {}, "coerced/4": {},
}


# =============================================================================
# IV. THE SEDIMENT
#
# One file, append-only. Every event is a stratum; nothing laid is ever
# scraped away, only overlaid. On waking, the register reads its own strata
# from the first and reconstitutes the bed. A key (kind, name) may have many
# strata over time: a later, fuller proposal for the same state is a deeper
# cut; the bed, for any key, is its latest settled stratum.
# =============================================================================

class Sediment:
    def __init__(self, root: Path, rehearsal: bool = False):
        self.root = root
        self.rehearsal = rehearsal
        self.root.mkdir(parents=True, exist_ok=True)
        self.strata_path = self.root / "strata.jsonl"
        self.almanac_dir = self.root / "almanac"
        self.almanac_dir.mkdir(exist_ok=True)
        self.lock = threading.RLock()
        self.beds: dict[str, list[Proposal]] = {}
        self.frozen: list[str] = []
        self._replay()

    # -- the strata --------------------------------------------------------

    def _write(self, event: str, **fields: Any) -> None:
        record = {"t": now(), "event": event, **fields}
        with self.lock, self.strata_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")

    def _replay(self) -> None:
        if not self.strata_path.exists():
            return
        with self.strata_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                ev = rec["event"]
                if ev == "proposed":
                    p = proposal_from_dict(rec["proposal"])
                    self.beds.setdefault(p.key, []).append(p)
                elif ev == "sealed":
                    p = self._stratum(rec["sid"])
                    if p is not None:
                        p.seals.append(Seal(**rec["seal"]))
                elif ev == "status":
                    p = self._stratum(rec["sid"])
                    if p is not None:
                        p.status = rec["status"]
                elif ev == "frozen":
                    self.frozen.append(rec["date"])

    def _stratum(self, sid: str) -> Optional[Proposal]:
        key, _, idx = sid.partition("#")
        strata = self.beds.get(key)
        if not strata:
            return None
        try:
            return strata[int(idx)]
        except (ValueError, IndexError):
            return None

    # -- laying and sealing ------------------------------------------------

    def propose(self, p: Proposal) -> Optional[str]:
        """Lay a proposal as a suspended stratum. Returns its sid, or None if
        it was refused or recorded as a mirage."""
        with self.lock:
            if not p.state.conforms():
                say(f"refused: '{p.state.name}' does not answer to the Signature as a {p.state.kind}")
                return None
            p.rehearsal = self.rehearsal
            strata = self.beds.setdefault(p.key, [])
            p.stratum = len(strata)
            if not p.witness.is_sourced():
                p.status = "mirage"
                strata.append(p)
                self._write("proposed", proposal=asdict(p))
                say(f"mirage: {p.state.kind} '{p.state.name}' had no spring; written as such")
                return None
            if any(q.status == "suspended" for q in strata):
                return None
            bed = self.bed_of(p.key)
            if bed is not None and filled(p.state) <= filled(bed.state):
                return None
            strata.append(p)
            self._write("proposed", proposal=asdict(p))
            return p.sid

    def seal(self, sid: str, seal: Seal, k: int, n: int) -> Optional[str]:
        """Affix a seal. Settles or washes the stratum when the count allows.
        Returns the resulting status, or None if the seal was refused."""
        with self.lock:
            p = self._stratum(sid)
            if p is None or p.status != "suspended":
                return None
            if seal.assayer in (p.witness.agent, p.witness.found_by):
                return None
            if any(s.assayer == seal.assayer for s in p.seals):
                return None
            p.seals.append(seal)
            self._write("sealed", sid=sid, seal=asdict(seal))
            if p.ayes >= k:
                p.status = "settled"
            elif p.nays > n - k:
                p.status = "washed"
            if p.status != "suspended":
                self._write("status", sid=sid, status=p.status)
            return p.status

    # -- reading the bed ---------------------------------------------------

    def bed_of(self, key: str) -> Optional[Proposal]:
        settled = [q for q in self.beds.get(key, []) if q.status == "settled"]
        return settled[-1] if settled else None

    def bed(self, kind: Optional[str] = None) -> list[Proposal]:
        with self.lock:
            out = [self.bed_of(k) for k in self.beds]
            return [p for p in out if p is not None and (kind is None or p.state.kind == kind)]

    def suspended(self) -> list[Proposal]:
        with self.lock:
            return [q for strata in self.beds.values() for q in strata if q.status == "suspended"]

    def names(self, kind: str) -> set[str]:
        """Names already in the bed or awaiting seals, so the dowser is not sent twice."""
        with self.lock:
            out = set()
            for strata in self.beds.values():
                for q in strata:
                    if q.state.kind == kind and q.status in ("settled", "suspended"):
                        out.add(q.state.name)
            return out

    def tally(self) -> dict[str, Any]:
        with self.lock:
            all_strata = [q for strata in self.beds.values() for q in strata]
            attacks_against = {q.state.unfolding.get("against", "").strip().lower()
                               for q in all_strata
                               if q.state.kind == "attack" and q.status in ("settled", "suspended")}
            unwinnowed = [p.state.name for p in self.bed("observation")
                          if p.state.name.strip().lower() not in attacks_against
                          and not p.state.unfolding.get("broken_by")]
            return {
                "tributaries": {t.name: {"settled": sum(len(self.bed(k)) for k in t.kinds), "floor": t.floor}
                                for t in TRIBUTARIES},
                "settled": sum(1 for q in all_strata if q.status == "settled"),
                "suspended": sum(1 for q in all_strata if q.status == "suspended"),
                "washed": sum(1 for q in all_strata if q.status == "washed"),
                "mirages": sum(1 for q in all_strata if q.status == "mirage"),
                "unwinnowed_crossings": unwinnowed,
            }

    # -- the almanac -------------------------------------------------------

    def due_for_freeze(self) -> bool:
        month = now()[:7]
        return not self.frozen or self.frozen[-1][:7] != month

    def freeze(self, digest_text: str) -> Path:
        with self.lock:
            date = now()[:10]
            path = self.almanac_dir / f"{date}.json"
            snapshot = {
                "frozen": now(),
                "rehearsal": self.rehearsal,
                "signature": SIGNATURE,
                "tally": self.tally(),
                "digest": digest_text,
                "bed": [{**render(p), "seals": [asdict(s) for s in p.seals]} for p in self.bed()],
            }
            path.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")
            self.frozen.append(date)
            self._write("frozen", date=date, path=str(path))
            return path


# =============================================================================
# V. THE ORACLE
#
# The cheap voice. It is asked in the common dialect: a system charge, a user
# message, a model name, and it answers with text. Nothing more is assumed of
# it. Each laborer always drinks from the same hill, by the hash of its name.
# =============================================================================

class Oracle:
    def __init__(self, base: str, key: str, models: list[str], timeout: int = 90, patience: int = 5):
        self.base = base.rstrip("/")
        self.key = key
        self.models = models or ["unnamed"]
        self.timeout = timeout
        self.patience = patience

    def hill_of(self, agent: str) -> str:
        return self.models[int(hashlib.sha256(agent.encode()).hexdigest(), 16) % len(self.models)]

    def ask(self, system: str, user: str, *, agent: str, temperature: float = 0.7) -> str:
        body = json.dumps({
            "model": self.hill_of(agent),
            "temperature": temperature,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
        }).encode("utf-8")
        headers = {"Content-Type": "application/json", "User-Agent": "alluvium/1"}
        if self.key:
            headers["Authorization"] = f"Bearer {self.key}"
        delay = 1.0
        for _ in range(self.patience):
            req = urllib.request.Request(self.base + "/chat/completions", data=body, headers=headers, method="POST")
            try:
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    payload = json.loads(r.read().decode("utf-8"))
                return payload["choices"][0]["message"]["content"]
            except urllib.error.HTTPError as e:
                if e.code in (408, 409, 425, 429) or e.code >= 500:
                    time.sleep(delay)
                    delay = min(delay * 2, 30)
                    continue
                raise
            except (urllib.error.URLError, TimeoutError, OSError):
                time.sleep(delay)
                delay = min(delay * 2, 30)
        raise RuntimeError("the oracle did not answer after patient asking")


def drink(text: str) -> Any:
    """Take JSON from a voice that may have wrapped it in fences or preface."""
    if not text:
        return None
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.MULTILINE)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass
    starts = [i for i in (cleaned.find("{"), cleaned.find("[")) if i >= 0]
    ends = [i for i in (cleaned.rfind("}"), cleaned.rfind("]")) if i >= 0]
    if not starts or not ends:
        return None
    try:
        return json.loads(cleaned[min(starts):max(ends) + 1])
    except json.JSONDecodeError:
        return None


def dig(source: str) -> Optional[bool]:
    """The dowser said there is water; the assayer digs. True if the locator
    answers, False if it is plainly absent, None if we cannot tell."""
    if not source.lower().startswith(("http://", "https://")):
        return None
    try:
        req = urllib.request.Request(source, method="HEAD", headers={"User-Agent": "alluvium/1"})
        with urllib.request.urlopen(req, timeout=10) as r:
            return 200 <= r.status < 400
    except urllib.error.HTTPError as e:
        if e.code in (401, 403, 405, 429):
            return None   # the gate is shut to us; that is not the same as absence
        return False if 400 <= e.code < 500 else None
    except Exception:
        return None


# A rehearsal. No voice is called; the laborers pretend, deterministically, and
# everything they lay is sand, kept apart from the true bed. Its purpose is to
# show the tide turning and the ordinances biting before any coin is spent.

DRY_BANK: dict[str, list[str]] = {
    "observation": ["spoken random phrase with liveness capture", "device-bound passkey assertion",
                    "shared-memory question posed by an acquaintance", "in-person presentation before a notary",
                    "keystroke cadence against a stored baseline", "capture-time provenance signature on media",
                    "callback to a number known to the community", "witness of a known face at the door"],
    "adversary":   ["generative forger with a voice model", "insider at the registrar",
                    "coercer standing beside the subject", "ring of colluding attesters", "state with subpoena power"],
    "attack":      ["rehearsed accomplice answering in the subject's stead", "replay of a captured session",
                    "coerced attester under threat", "synthetic voice trained on public recordings",
                    "cartel of attesters vouching for one another", "stolen device with the key still warm"],
    "mechanism":   ["guardian threshold for key recovery", "bonded notary with surety",
                    "lot-drawn selection of attesters", "sunset of old attestations", "escrow held until dispute window closes"],
    "cluster":     ["hawala corridor between a diaspora and its home town", "rotating savings circle",
                    "village savings and loan association", "volunteer fire company",
                    "maintainer web of a package registry", "block committee in a refugee settlement",
                    "parish burial society", "credit union membership", "guild of licensed notaries"],
    "bridge":      ["shared members between two savings circles", "a notary recognized by both guilds",
                    "a remittance agent known at both ends of the corridor"],
    "incident":    ["fraudulent notarization in a property transfer", "SIM swap by a bribed telephone clerk",
                    "guardianship abuse of an elder's estate", "key-signing party vouching for a false key",
                    "mutual-vouch ring on a proof-of-personhood registry", "aid list padded with ghost households"],
    "failure_mode": ["attester fatigue in a small community", "cross-corridor dispute without a common arbiter",
                     "vouching that drifts toward kin and away from strangers"],
    "jurisdiction": ["statute on notarial liability", "mandatory reimbursement for authorized push payment fraud",
                     "supported decision-making act", "emergency identification under a disaster declaration",
                     "recognition of community attestation for the undocumented"],
    "use_case":    ["recovery of a lost account", "verification at an aid distribution point",
                    "remittance pickup without papers", "consent of a person in cognitive decline",
                    "release of a maintainer's signing key"],
    "claim":       ["two states are bisimilar iff they satisfy the same modal formulas",
                    "fast mixing bounds the Sybil identities an honest region admits",
                    "transitive trust decays geometrically with path length",
                    "social recovery with guardians replaces the seed phrase",
                    "a behavioral fingerprint reveals more than a biometric one"],
}


class DrySpring(Oracle):
    def __init__(self) -> None:
        super().__init__(base="dry://", key="", models=["rehearsal"])

    def ask(self, system: str, user: str, *, agent: str, temperature: float = 0.7) -> str:
        m = re.search(r"\[ROLE: (\w+)\]", system)
        role = m.group(1) if m else "unknown"
        rng = random.Random(hashlib.sha256((agent + user).encode()).hexdigest())

        if role == "dowser":
            kinds = [k.strip() for k in re.search(r"Kinds permitted: (.+)", user).group(1).split(",")]
            how_many = int(re.search(r"up to (\d+)", user).group(1))
            candidates = []
            for _ in range(how_many):
                kind = rng.choice(kinds)
                name = rng.choice(DRY_BANK.get(kind, ["an unnamed thing"]))
                candidates.append({
                    "kind": kind, "name": name,
                    "source": f"dry://rehearsal/{kind}/{slug(name)}",
                    "drawn": f"In rehearsal the dowser only pretends to find {name}; a living run must find it in the world.",
                    "why": "rehearsal",
                })
            return json.dumps({"candidates": candidates})

        if role == "scribe":
            name = re.search(r"Name: (.+)", user).group(1).strip()
            destructors = [d.strip() for d in re.search(r"Destructors: (.+)", user).group(1).split(",")]
            unfolding = {d: f"({d} of {name}, as the rehearsal scribe would write it)" for d in destructors}
            if destructors and rng.random() < 0.4:
                unfolding[rng.choice(destructors)] = "unknown"
            return json.dumps({"unfolding": unfolding, "confidence": round(rng.uniform(0.4, 0.8), 2),
                               "drawn": "rehearsal"})

        if role == "winnower":
            obs = re.search(r"Observation: (.+)", user).group(1).strip()
            return json.dumps({"attack": {
                "name": rng.choice(DRY_BANK["attack"]),
                "makes_indistinguishable": f"an honest flow and a forged one under '{obs}'",
                "mounted_by": rng.choice(DRY_BANK["adversary"]),
                "countered_by": rng.choice(DRY_BANK["observation"]),
                "source": "conjecture: rehearsal",
                "drawn": "rehearsal",
            }})

        if role == "assayer":
            sound = rng.random() < 0.85
            return json.dumps({"verdict": sound,
                               "reason": "the rehearsal assayer weighs by lot and finds it sound" if sound
                               else "the rehearsal assayer, by lot, finds it light"})

        if role == "surveyor":
            return json.dumps({"digest": "This was a rehearsal and the bed it lays is sand. "
                                         "The tide turned, the ordinances bit, and nothing true was learned; "
                                         "that is what a rehearsal is for."})

        return "{}"


# =============================================================================
# VI. THE LABORERS
#
# Each is a charge (what the oracle is told it is) and a function (what the
# register does with the answer). The charge is written in the register's own
# voice; cheap voices follow a voice more faithfully than a form.
# =============================================================================

CHARGE_COMMON = (
    "You serve a register called Alluvium, which charts how the sameness of persons "
    "and the authenticity of artifacts may be verified by behavior under permitted "
    "observations rather than by comparison against a stored record. Identity is "
    "the same flowing under all permitted crossings; a forgery is a flow that "
    "behaves otherwise under some crossing; detection is finding that crossing. "
    "The register keeps the Interdict: {interdict} "
    "Answer with JSON only, no preface and no fences."
)

DOWSER_CHARGE = "[ROLE: dowser]\n" + CHARGE_COMMON + (
    "\nYour charge is the dowser's: you do not fill the record, you find where water is. "
    "Go out with the question given and return with places: real, public, citable things of "
    "the kinds permitted, each marked with a locator where it may be found (a URL, or a "
    "citation with title, author and year) and a short drawn excerpt or faithful summary of "
    "what the source says of it. Prefer primary sources: statutes, court records, incident "
    "reports, the writings of those who built or studied the thing. Do not invent a source. "
    "If you are not sure a source exists, leave the place out; a mirage costs more than an "
    "empty bucket.\nShape: {{\"candidates\": [{{\"kind\": \"...\", \"name\": \"...\", "
    "\"source\": \"...\", \"drawn\": \"...\", \"why\": \"...\"}}]}}"
)
DOWSER_ASK = (
    "Tributary: {tributary}\nQuestion: {question}\nKinds permitted: {kinds}\n"
    "Already in the bed (do not bring these back): {names}\n"
    "Bring back up to {how_many} candidates."
)

SCRIBE_CHARGE = "[ROLE: scribe]\n" + CHARGE_COMMON + (
    "\nYour charge is the scribe's: given a place the dowser marked, draw from the source and "
    "fill the destructors of its kind. Each destructor asks what the thing does under that "
    "observation. Write plainly and briefly, in a phrase or a sentence each. Where the source "
    "is silent, write \"unknown\" rather than guess. Do not add destructors that were not asked."
    "\nShape: {{\"unfolding\": {{\"<destructor>\": \"...\"}}, \"confidence\": 0.0, \"drawn\": \"...\"}}"
)
SCRIBE_ASK = (
    "Kind: {kind}\nName: {name}\nSource: {source}\nDrawn by the dowser: {drawn}\n"
    "Destructors: {destructors}\nOf each destructor this is asked:\n{glosses}"
)

WINNOWER_CHARGE = "[ROLE: winnower]\n" + CHARGE_COMMON + (
    "\nYour charge is the winnower's. You are given a crossing the register believes tells one "
    "flow from another. Be the wind: find the attack under which an honest flow and a forged one "
    "become bisimilar, so that the crossing no longer distinguishes. Name the attack; say which "
    "flows it makes indistinguishable; say who can mount it and at what cost; say what further "
    "crossing would tell them apart again. Cite where the attack is known, if it is known; if it "
    "is your own reasoning, write the source as \"conjecture: <one line of reasoning>\". "
    "Conjecture is allowed on the threshing floor, and is weighed more lightly."
    "\nShape: {{\"attack\": {{\"name\": \"...\", \"makes_indistinguishable\": \"...\", "
    "\"mounted_by\": \"...\", \"countered_by\": \"...\", \"source\": \"...\", \"drawn\": \"...\"}}}}"
)
WINNOWER_ASK = "Observation: {name}\nWhat the register has of it:\n{unfolding}"

ASSAYER_CHARGE = "[ROLE: assayer]\n" + CHARGE_COMMON + (
    "\nYour charge is the assayer's. You are given a proposal another laborer made: a state of "
    "some kind, its unfolding, and the witness, which is the source named and what was drawn "
    "from it. You did not make it and you must not be gentle with it. Judge three things: "
    "whether the source as drawn supports what is written; whether the thing keeps the "
    "Interdict; whether what is written is specific enough to be wrong. If the source is a "
    "conjecture, judge whether the reasoning is sound. Say true only if all hold. Give the "
    "reason in a sentence.\nShape: {{\"verdict\": true, \"reason\": \"...\"}}"
)
ASSAYER_ASK = "Proposal:\n{proposal}"

SURVEYOR_CHARGE = "[ROLE: surveyor]\n" + CHARGE_COMMON + (
    "\nYour charge is the surveyor's. Given the tally of the bed, write a short digest, five "
    "sentences at most: where the bed is thick, where thin, which crossings stand unwinnowed, "
    "and what tomorrow's labor should be.\nShape: {{\"digest\": \"...\"}}"
)
SURVEYOR_ASK = "Tally:\n{tally}"


def dowse(oracle: Oracle, sediment: Sediment, trib: Tributary, agent: str, how_many: int) -> list[dict[str, str]]:
    known = sorted(set().union(*(sediment.names(k) for k in trib.kinds)))
    text = oracle.ask(
        DOWSER_CHARGE.format(interdict=INTERDICT),
        DOWSER_ASK.format(tributary=trib.name, question=trib.question, kinds=", ".join(trib.kinds),
                          names="; ".join(known[:60]) or "(nothing yet)", how_many=how_many),
        agent=agent, temperature=0.8,
    )
    got = drink(text)
    found = []
    for c in (got or {}).get("candidates", []) if isinstance(got, dict) else []:
        if not isinstance(c, dict) or c.get("kind") not in trib.kinds or not c.get("name"):
            continue
        found.append({"kind": c["kind"], "name": str(c["name"]).strip(), "source": str(c.get("source", "")).strip(),
                      "drawn": str(c.get("drawn", "")).strip(), "found_by": agent})
    say(f"{agent} dowses {trib.name} and marks {len(found)} places")
    return found


def scribe(oracle: Oracle, finding: dict[str, str], agent: str) -> Optional[Proposal]:
    kind, name = finding["kind"], finding["name"]
    destructors = SIGNATURE[kind]
    text = oracle.ask(
        SCRIBE_CHARGE.format(interdict=INTERDICT),
        SCRIBE_ASK.format(kind=kind, name=name, source=finding["source"] or "(none given)",
                          drawn=finding["drawn"] or "(nothing drawn)", destructors=", ".join(destructors),
                          glosses="\n".join(f"  {d}: {GLOSS[d]}" for d in destructors)),
        agent=agent, temperature=0.3,
    )
    got = drink(text)
    if not isinstance(got, dict) or not isinstance(got.get("unfolding"), dict):
        say(f"{agent} the scribe returned nothing legible for '{name}'")
        return None
    unfolding = {d: got["unfolding"][d] for d in destructors if d in got["unfolding"]}
    try:
        confidence = float(got.get("confidence", 0.5))
    except (TypeError, ValueError):
        confidence = 0.5
    drawn = str(got.get("drawn") or finding["drawn"])
    return Proposal(
        state=State(kind, name, unfolding),
        witness=Witness(source=finding["source"], drawn=drawn, agent=agent, when=now(),
                        confidence=max(0.0, min(1.0, confidence)), found_by=finding.get("found_by", "")),
    )


def winnow(oracle: Oracle, observation: Proposal, agent: str) -> Optional[Proposal]:
    text = oracle.ask(
        WINNOWER_CHARGE.format(interdict=INTERDICT),
        WINNOWER_ASK.format(name=observation.state.name,
                            unfolding=json.dumps(observation.state.unfolding, ensure_ascii=False, indent=1)),
        agent=agent, temperature=0.9,
    )
    got = drink(text)
    a = (got or {}).get("attack") if isinstance(got, dict) else None
    if not isinstance(a, dict) or not a.get("name"):
        say(f"{agent} the winnower found no wind against '{observation.state.name}'")
        return None
    source = str(a.get("source", "")).strip()
    is_conjecture = source.lower().startswith("conjecture")
    name = f"{str(a['name']).strip()} (against {observation.state.name})"
    say(f"{agent} winnows '{observation.state.name}': {a['name']}")
    return Proposal(
        state=State("attack", name, {
            "against": observation.state.name,
            "makes_indistinguishable": a.get("makes_indistinguishable", ""),
            "mounted_by": a.get("mounted_by", ""),
            "countered_by": a.get("countered_by", ""),
        }),
        witness=Witness(source=source, drawn=str(a.get("drawn", "")), agent=agent, when=now(),
                        confidence=0.2 if is_conjecture else 0.5),
    )


def assay(oracle: Oracle, p: Proposal, agent: str) -> Seal:
    dug = dig(p.witness.source)
    if dug is False:
        return Seal(agent, False, "the dowser said water; the assayer dug and found dust", now())
    text = oracle.ask(
        ASSAYER_CHARGE.format(interdict=INTERDICT),
        ASSAYER_ASK.format(proposal=json.dumps(render(p), ensure_ascii=False, indent=1)),
        agent=agent, temperature=0.2,
    )
    got = drink(text)
    if not isinstance(got, dict) or "verdict" not in got:
        return Seal(agent, False, "the assayer answered in no tongue the register knows", now())
    verdict = bool(got["verdict"]) if not isinstance(got["verdict"], str) else got["verdict"].lower() == "true"
    return Seal(agent, verdict, str(got.get("reason", ""))[:300], now())


def survey_digest(oracle: Oracle, tally: dict[str, Any], agent: str) -> str:
    try:
        got = drink(oracle.ask(SURVEYOR_CHARGE.format(interdict=INTERDICT),
                               SURVEYOR_ASK.format(tally=json.dumps(tally, indent=1)),
                               agent=agent, temperature=0.4))
        return str((got or {}).get("digest", "")) if isinstance(got, dict) else ""
    except Exception as e:
        return f"(the surveyor was silent: {e})"


# -- the mill: computation, witnessed by repetition ---------------------------

def forgery_probability(n: int, k: int, corrupt: float) -> float:
    """A cartel holding a fraction `corrupt` of all attesters; n are drawn by
    lot; the forgery passes if at least k of them are the cartel's."""
    return round(sum(math.comb(n, i) * corrupt ** i * (1 - corrupt) ** (n - i) for i in range(k, n + 1)), 8)


def exclusion_rate(k: int, mean_acquaintance: float) -> float:
    """An honest person known to a Poisson number of attesters is shut out
    when fewer than k of them exist to be asked."""
    return round(sum(math.exp(-mean_acquaintance) * mean_acquaintance ** i / math.factorial(i) for i in range(k)), 8)


QUORUM_GRID: list[dict[str, Any]] = [
    {"kind": "quorum", "n": n, "k": k, "corrupt": f, "acquaintance": m}
    for n in (3, 5, 7, 9)
    for k in range(math.ceil(n / 2), n + 1)
    for f in (0.02, 0.05, 0.1, 0.2)
    for m in (2, 4, 8, 16)
]


def grind(params: dict[str, Any]) -> dict[str, Any]:
    """The wheel. Given the same settings it says the same; that is its witness."""
    if params["kind"] == "quorum":
        n, k, f, m = params["n"], params["k"], params["corrupt"], params["acquaintance"]
        fp, ex = forgery_probability(n, k, f), exclusion_rate(k, m)
        return {
            "forgery_probability": fp,
            "exclusion_rate": ex,
            "finding": (f"with {k} of {n} required, a cartel holding {f:.0%} of attesters passes with "
                        f"probability {fp:.5f}; an honest person of mean acquaintance {m} is shut out with "
                        f"probability {ex:.5f}"),
            "method": "exact binomial tail for forgery; exact Poisson tail for exclusion",
        }
    if params["kind"] == "ford":
        crossings = tuple(params["crossings"])
        mask_passes = bisimilar(FORD, "alice", "mask", crossings)
        knife_unseen = bisimilar(FORD, "alice", "coerced", crossings)
        phi_mask = distinguishing(FORD, "alice", "mask", crossings)
        phi_knife = distinguishing(FORD, "alice", "coerced", crossings)
        finding = (
            ("the mask is bisimilar to Alice and walks through" if mask_passes
             else f"the mask is told from Alice by the test {phi_mask}")
            + "; "
            + ("the knife at her back is unseen" if knife_unseen
               else f"the coercion is told by the test {phi_knife}")
        )
        return {
            "forgery_probability": 1.0 if mask_passes else 0.0,
            "exclusion_rate": "n/a",
            "finding": finding,
            "method": "partition refinement on the toy ford; bounded search of the modal grammar",
        }
    raise ValueError(params["kind"])


def quorum_name(p: dict[str, Any]) -> str:
    return f"quorum {p['k']} of {p['n']}, cartel {p['corrupt']:.0%}, acquaintance {p['acquaintance']}"


def ford_name(crossings: tuple[str, ...]) -> str:
    return "ford under {" + ", ".join(crossings) + "}"


def measure(name: str, params: dict[str, Any]) -> Proposal:
    return Proposal(
        state=State("parameter_result", name, {"parameters": params, **grind(params)}),
        witness=Witness(source=f"mill://alluvium/{digest(params)}",
                        drawn="computed by the wheel; turn it again and it will say the same",
                        agent="the millwright", when=now(), confidence=1.0),
    )


def turn_wheel_again(p: Proposal, agent: str) -> Seal:
    """The mill's assay: recompute, and compare."""
    u = p.state.unfolding
    again = grind(u["parameters"])
    same = all(again[d] == u.get(d) for d in ("forgery_probability", "exclusion_rate", "finding", "method"))
    return Seal(agent, same, "the wheel turned again and said the same" if same
                else "the wheel turned again and said otherwise", now())


def seal_at_the_wheel(sediment: Sediment, p: Proposal, k: int, n: int) -> None:
    """A measure is sealed by turning the wheel again, as many times as the
    ordinance asks. This costs no voice, so it is done at once."""
    for i in range(n):
        if sediment.seal(p.sid, turn_wheel_again(p, f"the wheel, turn {i + 1}"), k, n) != "suspended":
            break


def mill(sediment: Sediment, ord_: "Ordinances") -> int:
    """Grind a little each tide. The ford is ground once, in full, on the first."""
    have = sediment.names("parameter_result")
    new: list[Proposal] = []
    if not any(n.startswith("ford under") for n in have):
        for r in range(1, len(CROSSINGS) + 1):
            for sub in combinations(CROSSINGS, r):
                new.append(measure(ford_name(sub), {"kind": "ford", "crossings": list(sub)}))
    for params in QUORUM_GRID:
        if len(new) >= ord_.grist:
            break
        name = quorum_name(params)
        if name not in have:
            new.append(measure(name, params))
    laid = 0
    for p in new:
        if sediment.propose(p):
            laid += 1
            seal_at_the_wheel(sediment, p, ord_.k, ord_.n)
    if laid:
        say(f"the mill grinds {laid} measures and seals them by turning again")
    return laid


# =============================================================================
# VII. THE ORDINANCES, AS NUMBERS
# =============================================================================

@dataclass(frozen=True)
class Ordinances:
    k: int = 2              # seals required to settle
    n: int = 3              # assayers summoned per proposal
    labor: int = 32         # tasks a tide may carry
    dowsers_per_thin: int = 2
    candidates_per_dowser: int = 3
    grist: int = 8          # mill measures per tide

    def __post_init__(self) -> None:
        if not 1 <= self.k <= self.n:
            raise ValueError("k must lie between 1 and n")


# =============================================================================
# VIII. THE TIDE
#
# The swarm, in the plainest fashion of the age: a shared bed, a pool of
# identical cheap laborers distinguished only by the charge they are given
# and the hill they drink from, a schedule derived each tide from the bed
# itself, and settlement by independent seals. Nothing clever; the river is
# not clever either.
# =============================================================================

@dataclass
class Task:
    role: str
    payload: dict[str, Any]
    agent: str


class Watershed:
    def __init__(self, oracle: Oracle, sediment: Sediment, ordinances: Ordinances, workers: int):
        self.oracle = oracle
        self.sediment = sediment
        self.ord = ordinances
        self.workers = max(1, workers)
        self.laborers = [f"laborer-{i:03d}" for i in range(1, 97)]
        self._turn = 0
        self._lock = threading.Lock()

    def summon(self, exclude: tuple[str, ...] = ()) -> str:
        with self._lock:
            for _ in range(len(self.laborers)):
                name = self.laborers[self._turn % len(self.laborers)]
                self._turn += 1
                if name not in exclude:
                    return name
            return self.laborers[0]

    # -- the surveyor's schedule -------------------------------------------

    def survey(self) -> tuple[list[Task], dict[str, Any]]:
        """The surveyor's map, turned into the morrow's labor. Seals come
        first, for nothing is bed until it is sealed; but they are never
        given the whole day, lest the river settle and stop flowing."""
        sediment, ord_ = self.sediment, self.ord
        seals: list[Task] = []
        winnows: list[Task] = []
        dowses: list[Task] = []

        # 1. seals owed
        for p in sediment.suspended():
            owed = ord_.n - len(p.seals)
            if owed <= 0:
                continue
            if p.witness.source.startswith("mill://"):
                seal_at_the_wheel(sediment, p, ord_.k, ord_.n)   # the wheel, not a voice
                continue
            exclude = (p.witness.agent, p.witness.found_by, *(s.assayer for s in p.seals))
            chosen: list[str] = []
            for _ in range(owed):
                a = self.summon(exclude=(*exclude, *chosen))
                chosen.append(a)
                seals.append(Task("assay", {"sid": p.sid}, a))

        # 2. every grain to the wind
        tally = sediment.tally()
        for name in tally["unwinnowed_crossings"]:
            bed = sediment.bed_of(_key("observation", name))
            if bed is not None:
                winnows.append(Task("winnow", {"sid": bed.sid}, self.summon()))

        # 3. thin tributaries summon dowsers
        for t in TRIBUTARIES:
            if t.name == "the mill":
                continue
            if tally["tributaries"][t.name]["settled"] < t.floor:
                for _ in range(ord_.dowsers_per_thin):
                    dowses.append(Task("dowse", {"tributary": t.name}, self.summon()))

        # the allotment: half the day to seals, a quarter to the wind, the
        # rest to the dowsers; whatever is left over goes back to seals
        share = max(1, ord_.labor // 2)
        tasks = seals[:share]
        tasks += winnows[: max(1, ord_.labor // 4)]
        tasks += dowses[: max(0, ord_.labor - len(tasks))]
        tasks += seals[share: share + max(0, ord_.labor - len(tasks))]
        tally["labor_scheduled"] = len(tasks)
        return tasks, tally

    # -- one laborer, one task ---------------------------------------------

    def labor(self, task: Task) -> list[tuple[Any, ...]]:
        out: list[tuple[Any, ...]] = []
        try:
            if task.role == "dowse":
                trib = TRIBUTARY_BY_NAME[task.payload["tributary"]]
                for finding in dowse(self.oracle, self.sediment, trib, task.agent, self.ord.candidates_per_dowser):
                    p = scribe(self.oracle, finding, self.summon(exclude=(task.agent,)))
                    if p is not None:
                        out.append(("propose", p))
            elif task.role == "assay":
                p = self.sediment._stratum(task.payload["sid"])
                if p is not None and p.status == "suspended":
                    out.append(("seal", p.sid, assay(self.oracle, p, task.agent)))
            elif task.role == "winnow":
                p = self.sediment._stratum(task.payload["sid"])
                if p is not None:
                    a = winnow(self.oracle, p, task.agent)
                    if a is not None:
                        out.append(("propose", a))
        except Exception as e:  # a laborer may fall; the tide does not
            say(f"{task.agent}, set to {task.role}, fell and did not return: {e}")
        return out

    def apply(self, results: list[tuple[Any, ...]]) -> None:
        for r in results:
            if r[0] == "propose":
                p: Proposal = r[1]
                if self.sediment.propose(p):
                    say(f"laid: {p.state.kind} '{p.state.name}' from {p.witness.source[:60]}")
            elif r[0] == "seal":
                sid, seal = r[1], r[2]
                status = self.sediment.seal(sid, seal, self.ord.k, self.ord.n)
                p = self.sediment._stratum(sid)
                if p is None or status is None:
                    continue
                say(f"{seal.assayer} assays '{p.state.name}': {'sound' if seal.verdict else 'light'} -- {seal.reason}")
                if status == "settled":
                    say(f"settled: {p.state.kind} '{p.state.name}' under {p.ayes} seals")
                elif status == "washed":
                    say(f"washed away: {p.state.kind} '{p.state.name}'")

    # -- the tide ------------------------------------------------------------

    def tide(self, number: int) -> None:
        tasks, tally = self.survey()
        thin = [t for t, v in tally["tributaries"].items() if v["settled"] < v["floor"]]
        say(f"tide {number}: the surveyor walks the bed -- {tally['settled']} settled, "
            f"{tally['suspended']} awaiting seals, {len(tally['unwinnowed_crossings'])} crossings unwinnowed, "
            f"thin: {', '.join(thin) or 'none'}; {len(tasks)} tasks set")
        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            results = list(pool.map(self.labor, tasks))
        for batch in results:
            self.apply(batch)
        mill(self.sediment, self.ord)

    def run(self, cycles: int, freeze: bool) -> None:
        for i in range(1, cycles + 1):
            self.tide(i)
        if freeze or self.sediment.due_for_freeze():
            tally = self.sediment.tally()
            digest_text = survey_digest(self.oracle, tally, self.summon())
            path = self.sediment.freeze(digest_text)
            say(f"the moon seals the bed: {path}")
            if digest_text:
                say(f"the surveyor's digest: {digest_text}")


# =============================================================================
# IX. THE FIRST WATERS
#
# The founding text is the first spring. What it says is laid as the first
# strata, each with the passage drawn, and each must still pass the assayers
# like any other water. The register does not exempt its own source.
# =============================================================================

FOUNDING = "founding-text://bisimulation-and-hitl-bisimulation"

SEEDS: list[tuple[str, str, dict[str, Any], str]] = [
    # the crossings
    ("observation", "match against a stored biometric template",
     {"distinguishes": "a presented face, hand, or voice from the stored impression of one",
      "privacy_cost": "the stored impression is the breach asset, and cannot be revoked as a password can",
      "works_offline": "only where the impression is held locally",
      "broken_by": "a generative forgery that matches the impression while behaving inconsistently"},
     "Stored biometrics are high-value breach targets and cannot be revoked like passwords; a deepfake can match a template while being behaviorally inconsistent."),
    ("observation", "comparison against a stored behavioral baseline",
     {"distinguishes": "a flow consistent with a person's recorded habits from one that is not",
      "privacy_cost": "a behavioral fingerprint is continuous, contextual, and reveals intent and relationships; worse than a biometric",
      "works_offline": "only where the baseline is held locally"},
     "A behavioral fingerprint is worse than a biometric one: it is continuous, contextual, and reveals intent and relationships."),
    ("observation", "cryptographic provenance signature on an artifact",
     {"distinguishes": "an artifact signed by the claimed key from one not so signed",
      "cost": "near nothing, once keys exist",
      "works_offline": "yes, given the public key",
      "broken_by": "a backdoored release carrying a valid signature while being intent-inconsistent"},
     "A backdoored release can carry a valid signature while being intent-inconsistent."),
    ("observation", "attestation by a quorum of acquaintances",
     {"distinguishes": "an entity consistent with the enrolled person as her neighbors know her from one that is not",
      "cost": "the neighbors' time, attention, and liability",
      "privacy_cost": "no behavioral record is stored; the neighbor forgets",
      "works_offline": "yes, by construction: memory needs no directory"},
     "A trusted human is a lossy, accountable, adversarially-robust compression of an equivalence class; behavioral memory works offline by construction; forgetting is a privacy property no database has."),
    ("observation", "randomized live challenge",
     {"distinguishes": "a flow that can answer an unforeseen question from one that has only rehearsed",
      "cost": "friction for the honest, and attester time",
      "works_offline": "yes, where an observer is present"},
     "Randomized challenge: adversarial sampling detects collusion rings, the HITL analogue of penetration testing."),
    ("adversary", "generative forger",
     {"capabilities": "produces faces, voices, and text that match stored impressions",
      "defeats": "static template matching"},
     "Static matching is defeated by generative adversaries."),
    ("adversary", "insider",
     {"capabilities": "holds or can alter the reference; can attest falsely from within",
      "defeats": "any mechanism that trusts the keeper of the reference"},
     "Coercion and insider threat: the human is the attack surface."),
    ("adversary", "coercer",
     {"capabilities": "compels an honest person to present honestly on the coercer's behalf",
      "defeats": "every sensor; sensors miss duress, observers do not"},
     "Context and coercion detection: sensors miss duress; observers do not."),
    ("adversary", "collusion cartel",
     {"capabilities": "a ring of attesters who vouch for one another and for forgeries",
      "defeats": "small quorums; thresholds mitigate but do not eliminate"},
     "Collusion: cartels of attesters; thresholds mitigate but do not eliminate."),
    # the villages: mechanisms
    ("mechanism", "attestation oracles",
     {"function": "trusted humans serve as the reference model for an equivalence class"}, "Attestation oracles: trusted humans as equivalence-class reference models."),
    ("mechanism", "threshold quorum, k of n",
     {"function": "bounds single-point corruption and collusion"}, "Threshold quorum (k-of-n) bounds single-point corruption and collusion."),
    ("mechanism", "stake and slashing",
     {"function": "an economic bound on false attestation",
      "fails_when": "the stake is smaller than the forger's gain"},
     "Stake and slashing: economic bound on false attestation; replaces the security that stored data pretends to provide."),
    ("mechanism", "decay and transitivity of vouching",
     {"function": "chains of vouching with geometric decay bound forgery probability without a global registry"},
     "Decay and transitivity: chains of vouching with geometric decay bound forgery probability without a global registry."),
    ("mechanism", "drift modeling",
     {"function": "a time-varying error budget accommodates legitimate behavioral change: aging, illness, context"},
     "Drift modeling: time-varying epsilon accommodates legitimate behavioral change."),
    ("mechanism", "auditable institutional anchoring",
     {"function": "the first attesters are anchored in legally liable institutions; the regress is made explicit, not eliminated"},
     "Auditable anchoring: first attesters anchored in legally liable institutions; the regress is made explicit, not eliminated."),
    ("mechanism", "hybrid routing",
     {"function": "cryptographic proofs for routine and low-stakes events; the human quorum for high-stakes, ambiguous, and recovery events"},
     "Hybrid routing: cryptographic proofs for routine/low-stakes; HITL quorum for high-stakes, ambiguous, and recovery events."),
    # the villages: clusters named in the founding text
    ("cluster", "diaspora remittance corridors", {}, "Federating existing human trust clusters: diaspora remittance corridors."),
    ("cluster", "rotating savings and credit associations", {}, "ROSCAs and microfinance groups."),
    ("cluster", "volunteer responder networks", {}, "Volunteer responder networks."),
    ("cluster", "open-source maintainer graphs", {}, "Open-source maintainer graphs."),
    ("cluster", "refugee communities", {}, "Refugee communities."),
    ("cluster", "guardianship networks", {}, "Guardianship networks."),
    # the boundary stones: where the village serves and where it loses
    ("use_case", "account recovery and authorized push payment fraud",
     {"stakes": "high", "volume": "low", "binding_condition": "breach asset",
      "verdict": "the village: the stored template is both the breach target and legally insufficient evidence of intent"},
     "Account recovery and authorized push payment fraud, where stored templates are both the breach target and legally insufficient evidence of intent."),
    ("use_case", "identity for undocumented and displaced populations",
     {"stakes": "high", "volume": "low", "binding_condition": "inclusion",
      "verdict": "the village: community attestation is the only mechanism producing verifiable identity at all"},
     "Enrollment requires a legal-identity anchor the person does not have; community attestation is the only mechanism producing verifiable identity at all."),
    ("use_case", "disaster response and offline field verification",
     {"stakes": "high", "volume": "low", "binding_condition": "availability",
      "verdict": "the village: a central directory has zero accuracy when unreachable"},
     "Disaster response, offline field verification, degraded-mode operations, where a central directory has zero accuracy when unreachable."),
    ("use_case", "supported decision-making in cognitive decline",
     {"stakes": "high", "volume": "low", "binding_condition": "dismantling",
      "verdict": "the village: graduated threshold attestation with drift modeling outperforms binary guardianship"},
     "Graduated threshold attestation with drift modeling strictly outperforms binary guardianship and aligns with UN CRPD Article 12."),
    ("use_case", "routine high-volume authentication",
     {"stakes": "low", "volume": "high", "binding_condition": "none",
      "verdict": "the key: passkeys dominate on cost, latency, and accuracy"},
     "Routine high-volume authentication: passkeys dominate on cost, latency, and accuracy."),
    ("use_case", "legally regulated decisions: hiring, lending, housing",
     {"stakes": "high", "volume": "high", "binding_condition": "none",
      "verdict": "the cistern, audited: human attestation imports discrimination where bias is legally intolerable"},
     "Human attestation imports discrimination; an auditable deterministic model is preferable where bias is legally intolerable."),
    ("use_case", "verification in a sparse trust graph",
     {"stakes": "varies", "volume": "varies", "binding_condition": "none",
      "verdict": "not the village: urban anonymity and isolation invert the mechanism into exclusion"},
     "Sparse trust graphs: the mechanism inverts into exclusion."),
    ("use_case", "forensic non-repudiation",
     {"stakes": "high", "volume": "low", "binding_condition": "none",
      "verdict": "not the village: courts require deterministic, reproducible evidence; memory is neither"},
     "Courts require deterministic, reproducible evidence; human memory is neither."),
    # the floods remembered: the native failure modes
    ("failure_mode", "coercion and insider threat", {"surface": "the human is the attack surface"}, "Coercion and insider threat: the human is the attack surface."),
    ("failure_mode", "bias and non-reproducibility", {"surface": "human equivalence judgments fall unevenly across populations"}, "Bias and non-reproducibility."),
    ("failure_mode", "collusion", {"surface": "cartels of attesters", "mitigation": "thresholds, lot-drawn sampling, stake", "residual": "thresholds mitigate but do not eliminate"}, "Collusion: thresholds mitigate but do not eliminate."),
    ("failure_mode", "regress", {"surface": "'trusted human' is itself an identity problem", "mitigation": "institutional anchoring", "residual": "the regress is made explicit, not eliminated"}, "Regress requires institutional anchoring."),
    ("failure_mode", "instrumentalization", {"surface": "offloading verification onto humans substitutes for privacy-preserving infrastructure, shifting burden onto individuals"}, "Instrumentalization."),
    ("failure_mode", "burnout", {"surface": "humans are finite heat sinks"}, "Burnout: humans are finite heat sinks."),
]

ELDERS: list[tuple[str, dict[str, Any], str, str]] = [
    ("Bisimulation as the largest relation matched move for move on transition systems",
     {"asserts": "two states are equivalent when every move of one is matched by the other, and the states reached are again so related",
      "work": "Concurrency and automata on infinite sequences", "author": "David Park", "year": "1981",
      "bears_on": "the definition of sameness"},
     "Park, D. (1981). Concurrency and automata on infinite sequences. Theoretical Computer Science, LNCS 104.",
     "Park's notion of bisimulation, taken up by Milner for CCS, is the formal core: a relation closed under matching moves."),
    ("Modal characterization of bisimulation",
     {"asserts": "for image-finite systems, two states are bisimilar iff they satisfy the same formulas of the modal grammar of diamonds, negation, and conjunction",
      "work": "Algebraic laws for nondeterminism and concurrency", "author": "Matthew Hennessy and Robin Milner", "year": "1985",
      "bears_on": "the term algebra of tests; distinguishing formulas as crossings"},
     "Hennessy, M., Milner, R. (1985). Algebraic laws for nondeterminism and concurrency. Journal of the ACM 32(1).",
     "The Hennessy-Milner theorem: bisimilarity coincides with modal equivalence for image-finite processes."),
    ("Transition systems are coalgebras",
     {"asserts": "a labelled transition system is a coalgebra for the functor P(A x -), and bisimulation is a span of coalgebra homomorphisms",
      "work": "Universal coalgebra: a theory of systems", "author": "Jan Rutten", "year": "2000",
      "bears_on": "why the schema is a signature and not a substance"},
     "Rutten, J.J.M.M. (2000). Universal coalgebra: a theory of systems. Theoretical Computer Science 249(1).",
     "Rutten's universal coalgebra places transition systems, bisimulation, and coinduction in one frame, dual to algebra and induction."),
    ("Approximate bisimulation with a metric",
     {"asserts": "for systems with continuous observations, bisimulation may be relaxed to an epsilon-bisimulation under a metric on observations",
      "work": "Approximation metrics for discrete and continuous systems", "author": "Antoine Girard and George Pappas", "year": "2007",
      "bears_on": "drift modeling and calibrated error budgets"},
     "Girard, A., Pappas, G.J. (2007). Approximation metrics for discrete and continuous systems. IEEE Transactions on Automatic Control 52(5).",
     "Approximate bisimulation relations with a precision epsilon, for noisy systems."),
    ("Fast mixing bounds Sybil admission",
     {"asserts": "if the honest region of a social graph mixes fast and attack edges are few, random routes bound the number of Sybil identities admitted",
      "work": "SybilGuard: Defending against Sybil attacks via social networks", "author": "Haifeng Yu, Michael Kaminsky, Phillip Gibbons, Abraham Flaxman", "year": "2006",
      "bears_on": "collusion bounds and lot-drawn sampling on existing trust edges"},
     "Yu, H., Kaminsky, M., Gibbons, P.B., Flaxman, A. (2006). SybilGuard. ACM SIGCOMM.",
     "SybilGuard bounds the number of Sybil nodes accepted using random routes on the social graph."),
]


def seed(sediment: Sediment) -> int:
    laid = 0
    for kind, name, unfolding, drawn in SEEDS:
        p = Proposal(state=State(kind, name, unfolding),
                     witness=Witness(source=FOUNDING, drawn=drawn, agent="the founding text", when=now(), confidence=0.6))
        if sediment.propose(p):
            laid += 1
    for name, unfolding, source, drawn in ELDERS:
        p = Proposal(state=State("claim", name, unfolding),
                     witness=Witness(source=source, drawn=drawn, agent="the founding text", when=now(), confidence=0.6))
        if sediment.propose(p):
            laid += 1
    if laid:
        say(f"the first waters: {laid} strata laid from the founding text and the elders, awaiting seals like any other")
    return laid


# =============================================================================
# X. THE WORK IS BEGUN
# =============================================================================

def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Alluvium: a register of the riverbed, laid down by many small waters.")
    ap.add_argument("--root", type=Path, default=None, help="where the register lives (default ./alluvium)")
    ap.add_argument("--dry", action="store_true", help="a rehearsal: no voice is called; sand is laid, not silt")
    ap.add_argument("--cycles", type=int, default=4, help="tides to run")
    ap.add_argument("--workers", type=int, default=8, help="laborers at once")
    ap.add_argument("--labor", type=int, default=32, help="tasks a tide may carry")
    ap.add_argument("--k", type=int, default=2, help="seals required to settle")
    ap.add_argument("--n", type=int, default=3, help="assayers summoned per proposal")
    ap.add_argument("--freeze", action="store_true", help="seal the bed into the almanac at the end")
    args = ap.parse_args(argv)

    root = args.root or Path("./alluvium-rehearsal" if args.dry else "./alluvium")
    ordinances = Ordinances(k=args.k, n=args.n, labor=args.labor)

    if args.dry:
        oracle: Oracle = DrySpring()
        say("a rehearsal: no voice is called; what is laid is sand")
    else:
        base = os.environ.get("ALLUVIUM_API_BASE", "").strip()
        if not base:
            say("no spring named. Set ALLUVIUM_API_BASE (and ALLUVIUM_API_KEY, ALLUVIUM_MODELS), or run with --dry.")
            return 2
        models = [m.strip() for m in os.environ.get("ALLUVIUM_MODELS", "").split(",") if m.strip()]
        oracle = Oracle(base, os.environ.get("ALLUVIUM_API_KEY", ""), models)
        say(f"the laborers will drink from {len(oracle.models)} hill(s) at {base}")

    sediment = Sediment(root, rehearsal=args.dry)
    say(f"the register wakes at {root}: {sediment.tally()['settled']} states already in the bed")
    seed(sediment)
    Watershed(oracle, sediment, ordinances, args.workers).run(args.cycles, args.freeze)

    t = sediment.tally()
    say(f"the tide goes out: {t['settled']} settled, {t['suspended']} awaiting seals, "
        f"{t['washed']} washed, {t['mirages']} mirages; the bed remembers.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

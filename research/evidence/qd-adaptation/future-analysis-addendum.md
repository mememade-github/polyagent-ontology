# Future analysis addendum — authored after Stub

This is a NEW prospective definition, authored after run-001 and independent mechanical calculation, before any future real-model target access in this continuation. It is not backdated preregistration. The original protocol/lock/procedure/results/run-001 remain immutable. Hmechanical verdict is unchanged; actual model remains untested. Corpus, complete gold and actual token/time driver are absent, so science is NOT runnable.

## 1. Extractors and named selector claims (review request 1)

Hq-Fact is the main question: does QD coverage add value on a fixed Fact extractor? Hq-original is a separate selector claim inside the original concept extractor. For each seed 7/11/19 compare coverage versus random WITHIN the same extractor only. No pooled or cross-factor winner. Original uses the original concept prompt; fixed Fact adds only the instruction to set concept to Fact. General/qualifier lenses, schema, input pool, gates and caps are shared. Fact is excluded downstream by STOP_CONCEPTS; this trial cannot establish ontology improvement.

For EACH seed and EACH named claim independently retain the original thresholds: precision >= .90 and >= matched random; unique correct >= random + max(1,ceil(.10*random)); supported gold-cell recall >= random. A zero random baseline still needs one extra correct. Valid but unmet thresholds reject that operational claim on that sample; invalid controls, incomplete labels/accounting, missing gold or unresolved ambiguity are inconclusive. Paired seeds are not independent corpus samples.

## 2. Future freeze and blindness (review request 2)

The old lock froze mechanical rules before Stub, not a completed scientific preregistration. Before any future target run, freeze an independent heldout corpus, complete gold, input descriptors, context_dependent flags, annotation and adjudication plan, driver and their hashes. Gold annotators must be blinded to arm, selector, seed and model output until gold is complete. Later prediction judges are blinded to arm and selector, with preserved source and proposition provided. Known Acme/development gold is not blind. These are authored requirements, not completed procedures.

## 3. Independent quality and cell accounting (review request 3)

Independent complete adjudication deduplicates semantic equivalents for BOTH quality numerator and denominator. Let T be unique correct propositions and F unique incorrect propositions; precision=T/(T+F), empty output precision=0. Correct equivalence includes subject, relation, object, polarity, modality, condition and attribution. All predictions require adjudication; unresolved ambiguity or missing gold is inconclusive.

Gold-cell mapping uses pre-fixed input descriptor cells (sorted unique tags plus anchor bool), not output-discovered cells. Recall denominator is the set of input descriptor cells with at least one gold fact. Numerator is those cells supported by correct ACTIVE first-origin records. Denominator zero is inconclusive. Semantic dedup is independent adjudication, distinct from mechanical exact-string archive dedup.

## 4. Qualifiers and duplicates (review request 4)

Qualifier preservation is an input/prompt requirement with schema/span/VERIFY proxy checks; it is not mechanically proven semantic preservation. An exact archive duplicate attaches ONLY to the first active source cell; later provenance remains history and cannot inflate cell recall. Distinct propositions in one cell can remain active. Neither occupied cells nor VERIFY true proves correctness.

## 5. Resource accounting (review request 5)

Use the SAME BUDGET CAPS for each arm, report actual usage even when spending differs. Original hard limits are unchanged: 64 total attempted calls per arm, conservative prompt+reserved output <3800 each call, actual input+output <=64,000 tokens per arm, 900 seconds per arm. Reserve output and remaining total-token capacity BEFORE calls to prevent overflow; absent a sound bound/accounting abort as inconclusive. Exceptions/failed attempts consume caps. No truncation. Wall time means monotonic elapsed per arm from first request start to final response/end, including queue, load and controller time. The future driver is absent; these hard limits are not established by the current controller. Breach aborts/inconclusive. No real-model/API execution occurred here.

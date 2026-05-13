# .NET E-Filing Enhancement — Project Brief

## Initial outreach (from client)

> Good morning. I wanted to see if we could schedule some time this week to meet
> to see if you, Chris, can help us with some .NET programming. We currently
> have batching capabilities with Tyler, which is the state-provided e-filing
> provider. The issue that we are encountering is the ability to e-file more
> than two lead documents. At this time, we believe the best and cheapest route
> is to enhance this program. Our goal would also be to move our affidavits and
> motions to this program — that way, all e-file documents utilize the same
> program and process.
>
> This first meeting will be just an introduction to the project. I anticipate
> about 3–4 meetings to make sure everyone has a clear understanding and plan
> on how to help us better automate this e-filing system. It would be easier
> if every court had the same filing requirements, but that is not the case,
> which makes this process more complex. Nothing I don't think we can handle.

## What we know so far

- **Platform:** .NET (language/version TBD — likely C#; framework version TBD)
- **Current tool:** Tyler Technologies e-filing integration (state-provided
  provider) with existing batching capability
- **Pain point:** current program is limited to **2 lead documents** per filing;
  need to support more
- **Scope expansion:** bring **affidavits** and **motions** into the same
  program so every e-filed document type goes through one process
- **Complication:** filing requirements vary per court — the system must
  accommodate court-specific rules

## Open questions for kickoff meeting

1. Is the existing program source-available to us, or are we writing a wrapper
   / replacement?
2. Tyler integration surface — is it the **EFM (Electronic Filing Manager)**
   SOAP/REST API, the Odyssey File & Serve API, or a different interface?
3. Which states / courts are in scope on day one?
4. Auth model with Tyler (API key, certificate, OAuth)?
5. What does "lead document" mean in this jurisdiction's schema, and where
   does the 2-document limit actually live (Tyler's side, our code, or a
   court-specific config)?
6. Document storage / retention requirements (PII, court records retention).
7. Volume — filings per day/week, peak load?
8. Where do affidavits and motions live today (Word templates, another
   system, scanned PDFs)?

## Meeting plan

- **Meeting 1:** Introduction — high-level project, stakeholders, success
  criteria
- **Meetings 2–4:** Deep dives — current architecture, court rule variations,
  Tyler API specifics, proposed plan + estimate

## Notes

- Project workspace lives in this `dotnet-prep/` folder.
- The existing PCP-Nexus files in the repo root (build.py, build_body.py,
  index.html, parts/, template.html) are **read-only reference** for this
  effort — do not modify.

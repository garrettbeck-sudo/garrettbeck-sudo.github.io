# Change 2: Add Berkeley Haas Full-Time MBA education

## Goal

Update Garrett Beck's portfolio to show that he is attending UC Berkeley Haas's Full-Time MBA (FTMBA) program and expects to graduate in 2027.

## Branch

- Target branch: `IncludeBerkeleyEducation`
- The workspace is already on this branch; keep the implementation and verification there.

## Proposed change

1. Add an education credential to the About page for **UC Berkeley Haas School of Business — Full-Time MBA (FTMBA), expected Spring 2027**.
2. Add a concise, original description of the program based on Haas's official material: a rigorous, interdisciplinary business curriculum that develops leadership, business fundamentals, and applied learning.
3. Add a selected-coursework subsection, grouped by completed term, using course titles from the user-provided CalCentral academic summary:

   **Fall 2025**
   - Data and Decisions
   - Economics for Business Decision Making
   - Financial Accounting
   - Introduction to Finance
   - Leading People
   - Business Communication in Diverse Work Environments
   - Marketing

   **Spring 2026**
   - Macroeconomics in the Global Economy
   - Operations
   - Ethics and Responsibility in Business
   - Strategic Leadership
   - Strategic Brand Management
   - Selected Topics for MBA Students
   - Entrepreneurship

4. Add a short MBA/2027 education reference to the homepage overview and profile sidebar so the current program is visible from the main profile.

## Source notes

- The supplied CalCentral Academic Summary lists the MBA program and expected Spring 2027 graduation, and records the course titles above in Fall 2025 and Spring 2026.
- The supplied summary also lists Fall 2026 enrollment without grades; do not present those courses as completed coursework in this change.
- The public `https://calcentral.berkeley.edu/academics` page redirects to CalCentral sign-in. Use the user-provided summary only for the private academic record details.
- Haas program context comes from its official pages:
  - [Full-Time MBA](https://mba.haas.berkeley.edu/)
  - [Academics](https://mba.haas.berkeley.edu/academics)
  - [Curriculum](https://mba.haas.berkeley.edu/academics/curriculum)

## Content and privacy constraints

- Do not add course grades, GPA, units, grade points, or the CalCentral student ID.
- Do not copy or publish the academic-summary PDF; use only the relevant program and completed-course titles.
- Do not treat the listed Fall 2026 courses as completed.
- Leave the existing United States Military Academy education and recognition content unchanged.
- Keep the current static Jekyll site structure; do not add a backend or new framework.

## Acceptance criteria

- The About page identifies the program as the UC Berkeley Haas Full-Time MBA and clearly says expected graduation is 2027 (Spring 2027).
- Coursework shown is limited to the completed Fall 2025 and Spring 2026 course titles listed above.
- No Berkeley grades, GPA, units, grade points, student ID, or transcript PDF appear in the published site.
- The homepage and sidebar reflect the current MBA program.
- The Jekyll build succeeds, and the About and homepage layouts remain usable on desktop and mobile.
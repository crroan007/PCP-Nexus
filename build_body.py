#!/usr/bin/env python3
"""Builds the complete PCP Nexus Manual HTML body content."""
import os

TARGET = os.path.join(os.path.dirname(__file__), "index.html")

# Read the existing file (has CSS in head)
with open(TARGET, "r", encoding="utf-8") as f:
    content = f.read()

BODY = """
<header class="header">
  <div class="header-brand">
    <button class="header-menu-btn" onclick="toggleSidebar()" aria-label="Toggle navigation">
      <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <div class="header-logo">N</div>
    <span class="header-title">PCP Nexus</span>
    <span class="header-subtitle">User Manual</span>
  </div>
  <span class="header-version">v4.5 &mdash; March 2026</span>
</header>

<div class="sidebar-overlay" onclick="toggleSidebar()"></div>
<nav class="sidebar" id="sidebar">
  <div class="nav-section-label">Overview</div>
  <a class="nav-link" href="#welcome">Welcome</a>
  <a class="nav-link" href="#quick-start">Quick Start</a>
  <a class="nav-link" href="#roles">Your Role</a>
  <div class="nav-section-label">System</div>
  <a class="nav-link" href="#what-is-nexus">What Is PCP Nexus?</a>
  <a class="nav-link sub" href="#architecture">System Architecture</a>
  <a class="nav-link sub" href="#two-pipelines">The Two Pipelines</a>
  <a class="nav-link" href="#requirements">System Requirements</a>
  <div class="nav-section-label">Interface</div>
  <a class="nav-link" href="#main-window">The Main Window</a>
  <a class="nav-link" href="#console">Console Tab</a>
  <a class="nav-link" href="#settings">Settings</a>
  <div class="nav-section-label">Daily Operations</div>
  <a class="nav-link" href="#daily-procedures">Daily Procedures</a>
  <a class="nav-link" href="#phase1-workflow">Phase 1: Affidavits</a>
  <a class="nav-link" href="#phase2-workflow">Phase 2: Petitions</a>
  <a class="nav-link" href="#dashboard">Dashboard &amp; Reporting</a>
  <div class="nav-section-label">Advanced</div>
  <a class="nav-link" href="#deduplication">Deduplication</a>
  <a class="nav-link" href="#csv-handoff">CSV Handoff</a>
  <a class="nav-link" href="#backfill">Hourly Backfill</a>
  <a class="nav-link" href="#keywords">Keyword Monitoring</a>
  <div class="nav-section-label">Support</div>
  <a class="nav-link" href="#troubleshooting">Troubleshooting</a>
  <a class="nav-link" href="#checklists">Checklists</a>
  <a class="nav-link" href="#revision-history">Revision History</a>
</nav>

<main class="main">
<div class="content">

  <span class="section-anchor" id="welcome"></span>
  <div class="hero">
    <h1>PCP Nexus User Manual</h1>
    <p>Mission-critical document automation for court filings. This guide covers everything you need to operate, monitor, and maintain PCP Nexus &#8212; from daily checks to advanced configuration.</p>
    <div class="hero-meta">
      <span><span class="dot blue"></span> Version 4.5</span>
      <span><span class="dot green"></span> March 2026</span>
      <span>Professional Civil Process of Texas, Inc.</span>
    </div>
  </div>

  <span class="section-anchor" id="quick-start"></span>
  <div class="section">
    <h2><span class="section-number">01</span> Quick Start</h2>
    <p class="section-desc">Get the system running in four steps.</p>
    <ol class="steps">
      <li><div class="step-content"><strong>Open Outlook</strong><br>Launch Microsoft Outlook Classic and confirm it is logged into the correct mailbox. Outlook must be running as Administrator.</div></li>
      <li><div class="step-content"><strong>Launch PCP Nexus</strong><br>Open the PCP Nexus application from the desktop or Start menu.</div></li>
      <li><div class="step-content"><strong>Start the Engine</strong><br>Click <strong>Start Engine</strong> in the main window &#8212; or let Auto-Start handle it if enabled.</div></li>
      <li><div class="step-content"><strong>Verify the Status Bar</strong><br>Watch the footer status bar. Once it turns <strong style="color: var(--green-600);">green</strong>, the system is live and processing.</div></li>
    </ol>
    <div class="callout tip">
      <div class="callout-icon">&#128161;</div>
      <div class="callout-content">
        <strong>Tip</strong>
        <p>All settings, databases, logs, and backups live in <code>C:\\ProgramData\\PCP-Automation\\</code>. You should never need to navigate there during normal operations.</p>
      </div>
    </div>
  </div>

  <span class="section-anchor" id="roles"></span>
  <div class="section">
    <h2><span class="section-number">02</span> Your Role</h2>
    <p class="section-desc">PCP Nexus serves three types of users. Find your role and jump to the sections that matter most to you.</p>
    <div class="role-cards">
      <div class="role-card">
        <div class="role-card-icon operator">&#128100;</div>
        <h3>Operator</h3>
        <p>Daily monitoring, exception review, and confirming the nightly handover completed.</p>
        <a class="jump-link" href="#daily-procedures">Jump to Daily Procedures &rarr;</a>
      </div>
      <div class="role-card">
        <div class="role-card-icon supervisor">&#128101;</div>
        <h3>Supervisor</h3>
        <p>Validate compliance, spot-check outputs, and handle escalations flagged by operators.</p>
        <a class="jump-link" href="#dashboard">Jump to Dashboard &rarr;</a>
      </div>
      <div class="role-card">
        <div class="role-card-icon admin">&#9881;&#65039;</div>
        <h3>Administrator</h3>
        <p>Configuration changes, folder path updates, and advanced troubleshooting.</p>
        <a class="jump-link" href="#settings">Jump to Settings &rarr;</a>
      </div>
    </div>
    <div class="callout danger">
      <div class="callout-icon">&#9888;&#65039;</div>
      <div class="callout-content">
        <strong>Operators: Do Not Edit Configuration Files</strong>
        <p>Changes to configuration files can disrupt the entire pipeline. If something looks wrong, contact your Administrator.</p>
      </div>
    </div>
  </div>
"""

with open(os.path.join(os.path.dirname(__file__), "body_part1.txt"), "w", encoding="utf-8") as f:
    f.write(BODY)

print("Part 1 written OK")

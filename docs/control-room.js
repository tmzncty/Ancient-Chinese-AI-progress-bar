(() => {
  const OWNER = "tmzncty";
  const REPO = "Ancient-Chinese-AI-progress-bar";
  const params = new URLSearchParams(location.search);
  const ref = params.get("ref") || "main";
  const rawBase = `https://raw.githubusercontent.com/${OWNER}/${REPO}/${encodeURIComponent(ref)}`;

  const $ = (id) => document.getElementById(id);
  const escapeHtml = (value) => String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");

  const accessIcon = (value) => ({
    public: "✅ public",
    gated: "🔒 gated",
    partial: "◐ partial",
    unavailable: "✕ unavailable",
    unknown: "? unknown",
    not_applicable: "— n/a",
  }[value] || `? ${value}`);

  const bar = (level) => `${"█".repeat(Number(level))}${"░".repeat(5 - Number(level))}`;

  async function loadYaml(name) {
    const response = await fetch(`${rawBase}/${name}`, { cache: "no-store" });
    if (!response.ok) throw new Error(`${name}: HTTP ${response.status}`);
    return jsyaml.load(await response.text());
  }

  function renderSummary(progress, verification) {
    const caps = progress.capabilities || [];
    const sources = Object.values(verification.sources || {});
    const claims = Object.values(verification.claims || {});
    const reproduced = verification.reproduced_here || [];
    const gated = sources.filter((s) => s.data === "gated").length;

    $("summaryGrid").innerHTML = [
      [caps.length, "能力项（不求平均分）"],
      [sources.length, "已登记证据来源"],
      [claims.length, "显式数字/范围 claim"],
      [reproduced.length, "本站 claim 复现"],
    ].map(([number, label]) => `<div class="summary-card"><span class="number">${number}</span><span class="label">${label}</span></div>`).join("");

    const banner = $("reproductionBanner");
    banner.querySelector("strong").textContent = `本站复现：${reproduced.length} 项`;
    banner.querySelector("span").textContent = reproduced.length
      ? `已有 L4 记录；仍只对对应版本、数据与指标负责。另有 ${gated} 个来源的数据访问为 gated。`
      : `现在所有论文数字仍是报告值/物料核查值。另有 ${gated} 个来源的数据访问为 gated。`;
    if (reproduced.length) banner.classList.add("good");
  }

  function renderCapabilities(progress, verification) {
    const caps = progress.capabilities || [];
    const sourceAudits = verification.sources || {};
    const domains = ["all", ...new Set(caps.map((c) => c.domain))];
    let active = "all";

    const bestEvidenceLevel = (ids) => {
      const nums = (ids || []).map((id) => Number((sourceAudits[id]?.level || "L0").slice(1)));
      return nums.length ? `L${Math.max(...nums)}` : "L0";
    };

    const draw = () => {
      const visible = active === "all" ? caps : caps.filter((c) => c.domain === active);
      $("capabilityGrid").innerHTML = visible.map((c) => `
        <article class="capability">
          <div class="cap-top">
            <span class="cap-name">${escapeHtml(c.name_zh)}</span>
            <span class="cap-score"><span class="bar">${bar(c.level)}</span> ${c.level}/5</span>
          </div>
          <p>${escapeHtml(c.rationale)}</p>
          <div class="meta">
            <span class="pill">${escapeHtml(c.domain)}</span>
            <span class="pill">confidence: ${escapeHtml(c.confidence)}</span>
            <span class="pill">best evidence audit: ${bestEvidenceLevel(c.evidence)}</span>
            <span class="pill">evidence: ${(c.evidence || []).map(escapeHtml).join(", ")}</span>
          </div>
        </article>`).join("");
    };

    $("domainFilters").innerHTML = domains.map((d) => `<button data-domain="${escapeHtml(d)}" class="${d === active ? "active" : ""}">${escapeHtml(d)}</button>`).join("");
    $("domainFilters").addEventListener("click", (event) => {
      const button = event.target.closest("button[data-domain]");
      if (!button) return;
      active = button.dataset.domain;
      $("domainFilters").querySelectorAll("button").forEach((b) => b.classList.toggle("active", b === button));
      draw();
    });
    draw();
  }

  function renderSources(verification) {
    const sources = Object.entries(verification.sources || {})
      .sort((a, b) => Number(b[1].level.slice(1)) - Number(a[1].level.slice(1)) || a[0].localeCompare(b[0]));
    $("sourceTable").innerHTML = sources.map(([id, s]) => `
      <tr>
        <td><a href="${escapeHtml(s.primary)}" rel="noopener">${escapeHtml(id)}</a><br><small>${escapeHtml(s.title)}</small></td>
        <td class="level">${escapeHtml(s.level)}</td>
        ${["paper", "code", "data", "model"].map((field) => `<td class="access-${escapeHtml(s[field])}">${accessIcon(s[field])}</td>`).join("")}
        <td>${escapeHtml(s.reproduction)}</td>
      </tr>`).join("");
  }

  function renderClaims(verification) {
    const claims = Object.entries(verification.claims || {});
    $("claimGrid").innerHTML = claims.map(([id, c]) => `
      <article class="claim ${c.reproduced_here ? "reproduced" : ""}">
        <small>${escapeHtml(c.source)}</small>
        <span class="value">${escapeHtml(c.value)}</span>
        <strong>${escapeHtml(c.unit)}</strong>
        <p class="status">${escapeHtml(c.status)} · ${c.reproduced_here ? "本站已复现" : "本站未复现"}</p>
        <small>${escapeHtml(id)}</small>
      </article>`).join("");
  }

  function renderError(error) {
    const main = document.querySelector("main");
    const box = document.createElement("section");
    box.className = "error";
    box.innerHTML = `<strong>控制室读取失败：</strong> ${escapeHtml(error.message)}<br><small>可尝试 ?ref=main 或指定存在的 branch/tag。</small>`;
    main.prepend(box);
  }

  Promise.all([loadYaml("progress.yaml"), loadYaml("verification.yaml")])
    .then(([progress, verification]) => {
      $("lastUpdated").textContent = `CALIBRATED ${progress.updated || "?"}`;
      $("refLabel").textContent = `data ref: ${ref}`;
      renderSummary(progress, verification);
      renderCapabilities(progress, verification);
      renderSources(verification);
      renderClaims(verification);
    })
    .catch(renderError);
})();

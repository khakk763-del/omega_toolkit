#!/usr/bin/env python3
"""Instagram DM campaign sender — AI Lead Machine. Authorized by Khalid 2026-10-12 («قدم»).
Sends 12 personalized DMs, Gulf batch first then US/EU, ~10-15 min spacing. Logs to sent_log.md."""
import json, random, subprocess, sys, time
from datetime import datetime, timezone

ACCOUNT_ID = "17841447794505274"
BASE = "/home/hatch/workspace/goals/1000-2000/files/online_income/ig_dm_campaign_2026-10-12"
LOG = BASE + "/sent_log.md"

TARGETS = [
 ("donut.media", "17841403914169650",
  "مرحباً فريق Donut 👋 شفت شغلكم مع أكثر من 150 براند إماراتي — شغل قوي فعلاً، خصوصاً بالـF&B. لاحظت إن أغلب المطاعم تخسر حجوزات واستفسارات لأن المتابعة مع العميل تتأخر أو تنقطع. جهّزت حزمة AI Lead Machine: أنظمة n8n جاهزة للمتابعة التلقائية الفورية، وتقييم العملاء الجادين، وإحياء العملاء القدامى — تنركب بأقل من ساعة. https://payhip.com/b/Ig54k — هل هالشي يفيد عملاءكم بالمطاعم؟"),
 ("prismsocial", "17841400213425344",
  "هلا Prism 👋 شفت إنكم تقدّمون تدقيق مجاني للبراندات — فكرة ذكية لجذب العملاء. سؤالي: بعد ما يطلب العميل الـaudit، شلون تتم المتابعة معه؟ أغلب الوكالات تخسر هالنوع من العملاء بسبب بطء المتابعة. عندي حزمة AI Lead Machine: خمسة أنظمة n8n جاهزة للمتابعة الآلية الفورية وتقييم العملاء وإحياء القدامى. https://payhip.com/b/Ig54k — تحبون تشوفون إذا تناسب شغلكم؟"),
 ("socialstationme", "17841406248856082",
  "مرحباً 👋 عجبني توجهكم Human-AI-Transparency — نادر أشوف وكالة B2B بالمنطقة تتكلم عن الذكاء الاصطناعي بهالوضوح. جهّزت حزمة AI Lead Machine: خمسة workflows جاهزة على n8n للمتابعة الآلية للعملاء المحتملين وتقييمهم وإحياء القدامى منهم — تنركب على أي نظام موجود. https://payhip.com/b/Ig54k — هل تشوفون لها مكان ضمن حلول الـAI اللي تقدمونها لعملائكم؟"),
 ("stradauae", "17841440486442265",
  "مرحباً فريق Strada 👋 حسابكم يعكس صورة قوية للوساطة العقارية بدبي. سؤال من خبرة السوق: كم استفسار عقاري يوصلكم ويبرد قبل ما يرد عليه أحد؟ هذي أكبر خسارة بالعقارات. حزمة AI Lead Machine تسوي متابعة فورية آلية لكل استفسار، وتقيّم جدية المشتري، وترجع تتواصل مع العملاء القدامى تلقائياً. https://payhip.com/b/Ig54k — تستاهل التجربة على فريق مبيعاتكم؟"),
 ("goldmarkrealestate", "17841403371056727",
  "هلا Gold Mark 👋 Buy | Sell | Invest — واضح تركيزكم على المستثمر الجاد. المستثمر اللي يضغط إعلان اليوم وينتظر رد لبكرا غالباً يروح لمنافس. جهّزت نظام AI Lead Machine: متابعة فورية آلية + تقييم آلي لجدية العميل + إحياء العملاء القدامى، كله workflows جاهزة على n8n. https://payhip.com/b/Ig54k — هل هالنوع من الأتمتة يهمكم؟"),
 ("bsmartcreativeagency", "17841431907043583",
  "مرحباً BSMART 👋 شفت شغلكم بالتسويق الإبداعي وإدارة السوشيال ميديا — محتواكم واضح ومميز. سؤال سريع: عملاؤكم اللي تجيهم استفسارات من السوشيال ميديا، كيف يتابعون معها؟ حزمة AI Lead Machine عندي: خمسة أنظمة n8n جاهزة للمتابعة الفورية وتقييم العملاء وإحياء القدامى — ممكن تقدمونها كخدمة إضافية لعملائكم. https://payhip.com/b/Ig54k — تشوفونها مناسبة لوكالتكم؟"),
 ("disruptiveads", "17841401382619800",
  "Hi team 👋 Saw you're offering free Vision/Strategy/Execution audits — great way to pull in leads. Quick question: what happens after someone requests an audit? Most agencies lose those warm leads to slow follow-up. I built the AI Lead Machine: 5 ready-to-install n8n workflows for instant AI follow-up, lead scoring, and dead-lead revival. https://payhip.com/b/Ig54k — could this plug into how you handle inbound leads?"),
 ("webfx", "17841401910340291",
  "Hi WebFX team 👋 ROI-focused is exactly the right positioning — love it. I put together something your clients might like: the AI Lead Machine, 5 plug-and-play n8n workflows (instant lead follow-up, AI lead scoring, dead-lead revival, weekly reports) + 10 outreach scripts. It's built for agencies that live and die by measurable results. https://payhip.com/b/Ig54k — worth a look for your client work?"),
 ("lyfemarketing", "17841401558230721",
  "Hi 👋 Saw you do done-for-you social media for small businesses — that's a market that bleeds leads from slow follow-up. I built the AI Lead Machine: 5 ready n8n workflows for instant AI follow-up, lead scoring, and reviving cold leads, plus 10 outreach scripts. Could work as a new done-for-you service line for your clients. https://payhip.com/b/Ig54k — open to a quick look?"),
 ("smartbugmedia", "17841403094853004",
  "Hi team 👋 HubSpot Partner of the Year is no small feat — congrats. I built the AI Lead Machine: 5 n8n workflows (instant AI follow-up, lead scoring, dead-lead revival, weekly reporting) that sit nicely alongside a HubSpot stack for teams that want follow-up automation without another big platform bill. https://payhip.com/b/Ig54k — could it fit any of your client engagements?"),
 ("klientboost", "17841400315924132",
  "Hi 👋 You squeeze more ROI from paid ads — but what about the leads that come in after hours or go cold in the CRM? I built the AI Lead Machine: 5 ready n8n workflows for instant AI follow-up, lead scoring, and dead-lead revival + 10 outreach scripts. Built for performance marketers who hate leaking ad spend. https://payhip.com/b/Ig54k — worth 2 minutes of your time?"),
 ("wordstream", "17841402033820777",
  "Hi team 👋 You're the go-to for PPC data and insights — so you know the painful stat: most ad clicks never become conversations. I built the AI Lead Machine: 5 plug-and-play n8n workflows for instant AI follow-up, lead scoring, and reviving dead leads, plus 10 outreach scripts. Made for marketers who want more pipeline from the same ad spend. https://payhip.com/b/Ig54k — curious what you think?"),
]

def log(line):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"- [{ts}] {line}\n")
    print(line, flush=True)

def send_dm(username, fbid, text):
    cmd = ["instagram-messages-cli", "send", "--account-id", ACCOUNT_ID,
           "--recipient-user-fbids", fbid, "--text", text, "--retries", "2"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        out = (r.stdout or "")[:300]
        if r.returncode == 0:
            log(f"SENT @{username} — ok")
            return True
        log(f"FAILED @{username} — rc={r.returncode} err={(r.stderr or '')[:200]}")
        return False
    except Exception as e:
        log(f"FAILED @{username} — exception {str(e)[:150]}")
        return False

def main():
    import os
    start = int(os.environ.get("START_INDEX", "0"))
    log(f"CAMPAIGN START — {len(TARGETS)-start} DMs, Gulf batch first, ~12min spacing")
    for i in range(start, len(TARGETS)):
        username, fbid, text = TARGETS[i]
        ok = send_dm(username, fbid, text)
        if i < len(TARGETS) - 1:
            wait = random.randint(600, 900)
            log(f"waiting {wait//60}min before next")
            time.sleep(wait)
    log("CAMPAIGN END")

if __name__ == "__main__":
    main()

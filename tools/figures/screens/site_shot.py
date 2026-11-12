"""Capture a reader-site page in headless Chrome (CDP via press's check_layout)."""
import sys, json, base64
sys.path.insert(0, "/Users/clint/code/press/scripts")
from check_layout import Chrome, find_chrome
page, out, width, height, scale = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
clip_js = sys.argv[6] if len(sys.argv) > 6 else None
with Chrome(find_chrome()) as c:
    p, s = c._pipe, c._session
    p.call("Emulation.setDeviceMetricsOverride", {"width": width, "height": height, "deviceScaleFactor": scale, "mobile": False}, session=s)
    p.call("Emulation.setEmulatedMedia", {"features": [{"name": "prefers-color-scheme", "value": "light"}]}, session=s)
    c.navigate("file://" + page)
    c.evaluate("document.fonts.ready.then(()=>new Promise(r=>setTimeout(r,500)))")
    info = c.evaluate("""(()=>{const q=s=>{const e=document.querySelector(s);if(!e)return null;const r=e.getBoundingClientRect();return [s,Math.round(r.left),Math.round(r.top+scrollY),Math.round(r.width),Math.round(r.height)]};
      return ['header','.masthead','details','h1','main','article','figure','figure img','figcaption','nav.pager','.pager','body'].map(q).filter(Boolean)
      .concat([['theme',document.documentElement.dataset.theme||'',getComputedStyle(document.body).backgroundColor]])})()""")
    print(json.dumps(info))
    params = {"format": "png", "captureBeyondViewport": True}
    if clip_js:
        x, y, w, h = json.loads(clip_js)
        params["clip"] = {"x": x, "y": y, "width": w, "height": h, "scale": 1}
    data = p.call("Page.captureScreenshot", params, session=s)["data"]
    open(out, "wb").write(base64.b64decode(data))

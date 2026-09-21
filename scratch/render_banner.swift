import Foundation
import WebKit
import Cocoa

let htmlPath = "/Users/admin/Desktop/geminicli-backup/banniere_linkedin.html"
let outputPath = "/Users/admin/Desktop/geminicli-backup/banniere_linkedin_julien_florence.png"
let livrablePath = "/Users/admin/Desktop/geminicli-backup/04_Livrables/Images/banniere_linkedin_julien_florence.png"

let htmlURL = URL(fileURLWithPath: htmlPath)

let app = NSApplication.shared
app.setActivationPolicy(.prohibited)

class RenderDelegate: NSObject, WKNavigationDelegate {
    let webView: WKWebView
    
    init(webView: WKWebView) {
        self.webView = webView
    }
    
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        // Wait 1.5 seconds for Google Fonts & CSS animations to settle
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.5) {
            let config = WKSnapshotConfiguration()
            config.rect = CGRect(x: 0, y: 0, width: 1584, height: 396)
            
            webView.takeSnapshot(with: config) { image, error in
                if let image = image, let tiffData = image.tiffRepresentation, let bitmap = NSBitmapImageRep(data: tiffData), let pngData = bitmap.representation(using: .png, properties: [:]) {
                    try? pngData.write(to: URL(fileURLWithPath: outputPath))
                    try? pngData.write(to: URL(fileURLWithPath: livrablePath))
                    print("SUCCESS: Banner rendered successfully to \(outputPath)")
                } else {
                    print("ERROR rendering banner: \(String(describing: error))")
                }
                exit(0)
            }
        }
    }
}

let config = WKWebViewConfiguration()
let frame = CGRect(x: 0, y: 0, width: 1584, height: 396)
let webView = WKWebView(frame: frame, configuration: config)
let delegate = RenderDelegate(webView: webView)
webView.navigationDelegate = delegate

webView.loadFileURL(htmlURL, allowingReadAccessTo: htmlURL.deletingLastPathComponent())

RunLoop.main.run(until: Date().addingTimeInterval(5.0))

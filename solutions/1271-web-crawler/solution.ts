/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * class HtmlParser {
 *      getUrls(url: string): string[] {}
 * }
 */

function crawl(startUrl: string, htmlParser: HtmlParser): string[] {
    const res = new Set<string>()
    const visited = new Map()

    const hostName = new URL(startUrl).hostname;

    function dfs(url: string) {
        if (url.includes(hostName)) {
            res.add(url)
        }
        const urls = htmlParser.getUrls(url);

        if (!urls.length) {
            return
        }

        for (let u of urls) {
            if (!visited.has(u)&& u.includes(hostName)) {
                visited.set(u, true);

                dfs(u);
            }
        }
    }

    dfs(startUrl)


    return Array.from(res);
};

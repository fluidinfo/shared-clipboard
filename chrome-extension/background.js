var USERNAME = 'username'; // Change this to hold your Fluidinfo username.
var PASSWORD = 'password'; // Change this to hold your Fluidinfo password.

var fi = fluidinfo({ username: USERNAME, password: PASSWORD });
var tag = USERNAME + '/clipboard';


function getClickHandlerInsert() {
    return function(info, tab) {

        function success(results){
            // Send a message to the content script.
            obj = results.data[0];
            chrome.tabs.sendRequest(
                tab.id,
                obj[tag],
                function(what){ console.msg('Received response: ' + what); }
            );
        };

        var options = {
            select: [tag],
            where: 'has ' + tag,
            onSuccess: success,
            onError: function(result) { console.log(result); }
        };

        fi.query(options);
    };
};


function getClickHandlerSet() {
    return function(info, tab) {
        function saveClipboard(){
            var valuesArg = {};
            valuesArg[tag] = info.selectionText;
            var options = {
                values: valuesArg,
                about: '/' + USERNAME,
                onSuccess: function(result) { console.log('Tag set.'); },
                onError: function(result) { console.log(result); }
            };

            fi.tag(options);
        };

        var options = {
            tags: [tag],
            where: 'has ' + tag,
            onSuccess: saveClipboard,
            onError: function(result) {
                if (result.status === '404') {
                    saveClipboard();
                }
                else {
                    console.log(result.message);
                }
            }
        };

        fi.delete(options);
    };
};


function getClickHandlerClear() {
    return function(info, tab) {
        var options = {
            tags: [tag],
            where: 'has ' + tag,
            onSuccess: function(result) {},
            onError: function(result) {
                if (result.status !== '404') {
                    console.log(result.message);
                }
            }
        };

        fi.delete(options);
    };
};


// A context menu item for inserting the clipboard into editable objects.
chrome.contextMenus.create({
    'title' : 'Insert remote clipboard',
    'type' : 'normal',
    'contexts' : ['editable'],
    'onclick' : getClickHandlerInsert()
});

// A context menu item for saving the selection to the clipboard.
chrome.contextMenus.create({
    'title' : 'Save selection to remote clipboard',
    'type' : 'normal',
    'contexts' : ['selection'],
    'onclick' : getClickHandlerSet()
});

// A context menu item for clearing the clipboard.
chrome.contextMenus.create({
    'title' : 'Clear remote clipboard',
    'type' : 'normal',
    'contexts' : ['editable'],
    'onclick' : getClickHandlerClear()
});

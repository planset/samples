
/**
 * print
 * console.logでも同じようなもん
 */
var print = function (message) {
    process.stdout.write(String(message) + "\n");
};

/** 
 * assertTrue
 */
var assertTrue = function (condition, message) {
    message = message || 'ERROR';
    if (condition !== true) {
        throw new Error(message);
    }
};

/** 
 * assertFalse
 */
var assertFalse = function (condition, message) {
    message = message || 'ERROR';
    if (condition !== false) {
        throw new Error(message);
    }
};

/** 
 * assertArrayEqual
 */
var assertArrayEqual = function (a, b, message, comp) {
    if (a.length !== b.length) {
        throw new Error(message);
    }
    if (typeof comp === 'undefined') {
        comp = function(a, b){
            return a === b;
        };
    }
    for (var i = 0; i < a.length; i += 1) {
        if (!comp(a[i], b[i])) {
            throw new Error(message + '  i=' + i + ', a = ' + a + ', b = ' + b);
        }
    }
};

/** 
 * assertEqual
 */
var assertEqual = function (a, b, message) {
    message = message || 'ERROR ' + a + ' != ' + b;

    if (is_array(a) && is_array(b)) {
        return assertArrayEqual(a, b, message);
    }

    if (a != b) {
        throw new Error(message);
    }
};

/** 
 * printObj
 * 
 * @param {obj} some object
 * 
 * Output to console.log 
 */
var printObj = function (obj) {
    var out = '';
    for (var p in obj) {
        out += p + ': ' + obj[p] + '\n';
    }
    console.log(out);
};

/**
 * create
 */
if (typeof Object.create !== 'function') {
    Object.create = function () {
        var F = function () {};
        F.prototype = o;
        return new F();
    };
}

/** 
 * method
 * @param {string} method name
 * @param {function} method function
 * @return {function} method
 */
Function.prototype.method = function (name, func) {
    if (!this.prototype[name]) {
        this.prototype[name] = func;
        return this;
    }
};

/** 
 * superior
 */
Object.method('superior', function (name) {
    var that = this;
    var method = that[name];
    return function () {
        return method.apply(that, arguments);
    };
});

/** 
 * eventuality
 */
var eventuality = function (that) {
    var registry = {};

    that.fire = function (event) {
        var array,
        func,
        handler,
        i,
        type = typeof event === 'string' ? event : event.type;

        if (registry.hasOwnProperty(type)) {
            array = registry[type];
            for (i = 0; i < array.length; i += 1) {
                handler = array[i];
                func = handler.method;
                if (typeof func === 'string') {
                    func = this[func];
                }
                func.apply(this, handler.parameters || [event]);
            }
        }
        return this;
    };
    that.on = function(type, method, parameters) {
        var handler = {
            method: method,
            parameters: parameters
        };
        if (registry.hasOwnProperty(type)) {
            registry[type].push(handler);
        } else {
            registry[type] = [handler];
        }
        return this;
    };

    return that;
};

/** 
 * reduce
 */
Array.method('reduce', function (f, value) {
    var i;
    for (i = 0; i < this.length; i += 1) {
        value = f(this[i], value);
    }
    return value;
});

/** 
 * is_array
 * p70
 */
var is_array = function (value) {
    if (Object.prototype.toString.apply(value) === '[object Array]') {
        return true;
    }
    return false;
};
assertTrue(is_array([]));
assertFalse(is_array(3));
assertFalse(is_array(null));

/** 
 * is_object
 * 
 * The value is not null and the value is object.
 * p120
 */
var is_object = function (value) {
    if (value && typeof value === 'object') {
        return true;
    }
    return false;
};
assertTrue(is_object({}));
assertTrue(is_object([]));
assertFalse(is_object(3));
assertFalse(is_object(null));

/** 
 * is_number
 * 
 * isNaN
 */
var is_number = function (value) {
    if (typeof value === 'number' && isFinite(value)) {
        return true;
    }
    return false;
};
assertTrue(is_number(3));
assertFalse(is_number('3'));
assertFalse(is_number(null));

/** 
 * dim 
 *
 * @param {dimension} dimension
 * @param {initial} initial value
 *
 * p73
 */
Array.dim = function (dimension, initial) {
    var a = [], i;
    for (i = 0; i < dimension; i += 1) {
        a[i] = initial;
    }
    return a;
};

/** 
 * matrix
 */
Array.matrix = function (m, n, initial) {
    var a, i, j, mat = [];
    for (i = 0; i < m; i += 1) {
        a = [];
        for (j = 0; j < n; j += 1) {
            a[j] = initial;
        }
        mat[i] = a;
    }
    return mat;
};


/** 
 * entityify
 * 
 * p104 
 */
String.method('entityify', function () {
    var character = {
        '<' : '&lt;',
        '>' : '&gt;',
        '&' : '&amp;',
        '"' : '&quot;'
    };
    return function () {
        return this.replace(/[<>&"]/g, function(c){
            return character[c];
        });
    };
}());


/*
 * Timer
 */
var timer = function(){

    var start,
        end;
    
    return {
        start: function(){
            start = new Date().getTime();
        },
        stop: function(){
            end = new Date().getTime();
            return this.getTime();
        },
        getTime: function(){
            var time = end - start;
            return time;
        }
    };
};

/** 
 * p24
 */
var p24 = function () {
    var flight = {
        airline: 'Oceanic',
        number: 815,
        departure: {
            IATA: 'SYD',
            time: '2004-09-23 14:55',
            city: 'Sydney'
        },
        arrival: {
            IATA: 'LAX',
            time: '2004-9-23 10:42',
            city: 'Los Angeles'
        }
    };
    assertEqual('SYD', flight.departure.IATA);
};
p24();


var p34 = function () {
    Number.method('integer', function(){
        return Math[this < 0 ? 'ceil' : 'floor'](this);
    });
    assertEqual(-3, (-10/3).integer());

    String.method('trim', function (){
        return this.replace(/^\s+|\s+$/g, '');
    });
    assertEqual('hoge', " hoge ".trim());
};
p34();


var p42 = function (){
    var myObject = function () {
        var value = 0;

        return {
            increment: function (inc) {
                value += typeof inc === 'number' ? inc : 1;
            },
            getValue: function () {
                return value;
            }
        };
    }();

    assertEqual(0, myObject.getValue());
    myObject.increment();
    assertEqual(1, myObject.getValue());
};
p42();


var p46 = function () {
    var value = -1;
    var add_the_handlers = function (nodes) {
        var helper = function (i) {
            return function (e) {
                value = i;
            };
        };
        for (var i = 0; i < nodes.length; i += 1) {
            nodes[i].onclick = helper(i);
        }
    };

    var nodes = [{}, {}];
    add_the_handlers(nodes);
    nodes[0].onclick();
    assertEqual(0, value);
    nodes[1].onclick();
    assertEqual(1, value);
};
p46();

var p48 = function () {
    var serial_maker = function () {
        var prefix = '';
        var seq = 0;
        return {
            set_prefix: function (p) {
                prefix = String(p);
            },
            set_seq: function (s) {
                seq = s;
            },
            gensym: function () {
                var result = prefix + seq;
                seq += 1;
                return result;
            }
        };
    };

    var seqer = serial_maker();
    seqer.set_prefix('Q');
    seqer.set_seq(1000);
    var unique = seqer.gensym();

    assertEqual('Q1000', unique);
};
p48();


var p52 = function () {
    var memoizer = function (memo, fundamental) {
        var shell = function (n) {
            var result = memo[n];
            if (typeof result !== 'number') {
                result = fundamental(shell, n);
                memo[n] = result;
            }
            return result;
        };
        return shell;
    };
    var fibonacci_normal = function (n) {
        return n < 2 ? n : fibonacci_normal(n - 1) + fibonacci_normal(n - 2);
    };
    var fibonacci_memo = memoizer([0, 1], function (shell, n) {
        return shell(n - 1) + shell(n - 2);
    });
    var t = timer();

    t.start();
    fibonacci_normal(30);
    var time_normal = t.stop();

    t.start();
    fibonacci_memo(1000);
    var time_memo = t.stop();

    assertTrue(time_normal > time_memo);
};
p52();

var p63 = function () {
    var cat = function (spec) {
        var that = this;
        that.get_name = function () {
            return 'hoge';
        };
        return that;
    };
    var coolcat = function (spec) {
        var that = cat(spec);
        var super_get_name = superior('get_name');
        that.get_name = function (n) {
            return 'like ' + super_get_name() + ' baby';
        };
        return that;
    };
    var myCoolCat = coolcat({name: 'Bix'});
    var name = myCoolCat.get_name();
    assertEqual('like hoge baby', name);
};
p63();


var p64 = function () {
    var logs = '';
    var o = {};
    eventuality(o);
    o.on('message', function(e){
        return logs += e.message;
    });
    var ret = o.fire({
        type: 'message',
        message: 'hoge'
    });
    assertEqual('hoge', logs);
};
p64();

var p68 = function () {
    var numbers = [] ;
    numbers[0] = 1;
    assertEqual(1, numbers.length);
    numbers[5] = 5;
    assertEqual(6, numbers.length);
    numbers.push(6);
    assertEqual(7, numbers.length);
    delete numbers[0];
    assertEqual(7, numbers.length);
    numbers.splice(2, 1);
    assertEqual(6, numbers.length);
};
p68();

var p71 = function () {
    var numbers = [1, 2, 3, 4];
    assertTrue(is_array(numbers));
    assertFalse(is_array(1));

    var ret = numbers.reduce(function (v1, v2) {
        return v1 + v2;
    }, 0);
    assertEqual(10, ret);
};
p71();


var p103 = function () {
    var data = [4, 8, 15, 16, 23, 42];
    var add = function (a, b) {
        return a + b;
    };
    var mult = function (a, b) {
        return a * b;
    };
    var sum = data.reduce(add, 0);
    var product = data.reduce(mult, 1);
    data.total = function () {
        return this.reduce(add, 0);
    };
    var total = data.total();
    assertEqual(108, sum);
    assertEqual(7418880, product);
    assertEqual(108, total);
};
p103();

var p73 = function () {
    var myArray = Array.dim(10, 0);
    assertEqual(myArray, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]);
};
p73();

var p74 = function () {
    var myMatrix = Array.matrix(4, 4, 0);
    for (var i = 0; i < myMatrix.length; i += 1) {
        assertEqual(myMatrix[i], [0, 0, 0, 0]);
    }
};
p74();


var p76 = function () {
    var parse_url = /^(?:([A-Za-z]+):)?(\/{0,3})([0-9.\-A-Za-z]+)(?::(\d+))?(?:\/([^?#]*))?(?:\?([^#]*))?(?:#(.*))?$/;
     var url = 'http://www.ora.com:80/goodparts?q#fragment';
     var result = parse_url.exec(url);
     var i = 0;
     assertEqual(8, result.length);
     assertEqual(url, result[i]); i += 1;
     assertEqual('http', result[i]); i += 1;
     assertEqual('//', result[i]); i += 1;
     assertEqual('www.ora.com', result[i]); i += 1;
     assertEqual('80', result[i]); i += 1;
     assertEqual('goodparts', result[i]); i += 1;
     assertEqual('q', result[i]); i += 1;
     assertEqual('fragment', result[i]); i += 1;
};
p76();


var p92 = function (){
    var by = function (name) {
        return function(o, p){
            var a, b;
            if (typeof o === 'object' && typeof p === 'object' && o && p) {
                a = o[name];
                b = p[name];
                if (a === b) {
                    return 0;
                }
                if (typeof a === typeof b) {
                    return a < b ? -1 : 1;
                }
                return typeof a < typeof b ? -1 : 1;
            } else {
                throw {
                    name: 'Error',
                    mesage: name + ' を含むオブジェクトが必要です。'
                };
            }
        };
    };

    var s = [
        {first: 'Joe', last: 'Besser'},
        {first: 'Moe', last: 'Howard'},
        {first: 'Joe', last: 'DeRita'},
        {first: 'Shemp', last: 'Howard'},
        {first: 'Larry', last: 'Fine'},
        {first: 'Curly', last: 'Howard'}
    ];

    s.sort(by('first'));

    var comp = function (a, b) {
        return a.first === b.first && a.last === b.last;
    };

    assertArrayEqual([
        {first: 'Curly', last: 'Howard'},
        {first: 'Joe', last: 'Besser'},
        {first: 'Joe', last: 'DeRita'},
        {first: 'Larry', last: 'Fine'},
        {first: 'Moe', last: 'Howard'},
        {first: 'Shemp', last: 'Howard'}
    ], s, '', comp);

};
p92();


var p94 = function (){
    var by = function (name, minor) {
        return function(o, p){
            var a, b;
            if (typeof o === 'object' && typeof p === 'object' && o && p) {
                a = o[name];
                b = p[name];
                if (a === b) {
                    return typeof minor === 'function' ? minor(o, p) : 0;
                }
                if (typeof a === typeof b) {
                    return a < b ? -1 : 1;
                }
                return typeof a < typeof b ? -1 : 1;
            } else {
                throw {
                    name: 'Error',
                    mesage: name + ' を含むオブジェクトが必要です。'
                };
            }
        };
    };

    var s = [
        {first: 'Moe', last: 'Howard'},
        {first: 'Joe', last: 'DeRita'},
        {first: 'Shemp', last: 'Howard'},
        {first: 'Joe', last: 'Besser'},
        {first: 'Larry', last: 'Fine'},
        {first: 'Curly', last: 'Howard'}
    ];

    s.sort(by('last', by('first')));

    var comp = function (a, b) {
        return a.first === b.first && a.last === b.last;
    };

    assertArrayEqual([
        {first: 'Joe', last: 'Besser'},
        {first: 'Joe', last: 'DeRita'},
        {first: 'Larry', last: 'Fine'},
        {first: 'Curly', last: 'Howard'},
        {first: 'Moe', last: 'Howard'},
        {first: 'Shemp', last: 'Howard'}
    ], s, '', comp);

};
p94();


/** 
 * entityifyのテスト
 * replaceで見つけた内容を変換している.
 */
var p105 = function () {
    assertEqual('&lt;&amp;&gt;', "<&>".entityify());
};
p105();


